"""
All the functions that pull information from or save information to files 
"""
try:
    from main_build.dependencies.data import Equipment
    from main_build.dependencies.gui import Popup 
except:
    from data import Equipment
    from gui import Popup 
from openpyxl import Workbook as xlwkbk
from openpyxl import load_workbook
from datetime import date
import csv

def save_eqpt_to_csv(values, filepath, unique_report_name):
    """
    Saves the equipment currently being reported to a csv file
    """
    cur_date = date.today()
    header = False
    # check if header needs to be generated (happens when the file hasn't been
    # created before)
    try:
        with open(filepath, "r", newline="") as f:
            pass
    except Exception as e:
        header = True #header needs to be generated
    with open(filepath, "a", newline="") as f:
        csv_writer = csv.writer(f)
        #write the header line
        if header: csv_writer.writerow(["Date", "Project Number", "Equipment Number", "Equipment Tags", "Tags", "Name", "Mounting Location", "File Name"])
        try:
            new_row = [ #create the new row
                cur_date,
                values['project_number'][0],
                values['eqpt_number'][0],
                values['eqpt_tags'][0].upper(), 
                values['tags'][0].upper(),
                values['eqpt_name'][0].upper(),
                values['mounting_location'][0].upper(),
                unique_report_name + ".mcdx",
            ]
        except Exception as e:
            print(e)
        csv_writer.writerow(new_row) #insert the new row
    f.close() #necissary to close the file
    return True


def get_eqpt_from_xl(filepath: str) -> Equipment:
    """
    Gets all the equipment from an excel file and returns an equipment object
    """
    wb = load_workbook(filename=filepath)
    try: sheet = wb['values'] # set worksheet to the values sheet
    except: sheet = wb['Calculation']
    # iterate through each of the equipment and append it to the object
    headers = list()
    equipment = Equipment() # new equipment class

    """
    Search for header row before finding data
    """
    header_row = None 
    for idx, row in enumerate(sheet.iter_rows(values_only=True)):
        #gow through each row in the excel worksheet
        if row[0] == "eqpt_name":
            headers = list(row)  # will search for header row, then start to take data from the rest of the rows
            # Clean up headers variable by removing all errananeous items
            while "" in headers:
                headers.remove("")
            while None in headers:
                headers.remove(None)
            while " " in headers:
                headers.remove(" ")
            required_headers = ["eqpt_name", "project_number", 'eqpt_tags', "tags", "eqpt_number", "mounting_location"]
            for required_header in required_headers:
                if required_header not in headers: #error
                    alert = Popup("Error", "You must include the following column headers in your excel input file: eqpt_name, project_number, 'eqpt_tags', tags, eqpt_number, mounting_location")
                    alert.alert() #alert the user of their mistake 
                    return equipment #return a blank equipment 

            header_row = idx  #we found the start of the useful information
        #if we found the header row and the current row is not blank
        elif header_row and row[0] is not None:
            cur_eqpt = dict()
            for i, header in enumerate(headers):
                # populates each eqpt with the input fields and [value, units]
                try:
                    units = header.split("(")[1]
                    units = units.strip(")")
                    field = header.split("(")[0]
                    field = field.strip(" ")
                    comment = sheet.cell(row = header_row+1, column = i+1).comment 
                    from main_build.dependencies import helpers 
                    try: comment = helpers.format_comment(comment.text)
                    except: pass 
                    cur_eqpt[field] = [row[i], units, comment]  # assign cur_eqpt
                except:
                    cur_eqpt[header] = [row[i], "", ""]  # <- blank units
            equipment.append(cur_eqpt)
        elif header_row and row[0] is None:
            break  # want to break out and not view all rows when reached end of eqpt list
    return equipment

def save_eqpt_to_xl(equipment: Equipment, filepath:str)->bool:
    """
    Saves the equipment back to the excel file
    """
    wb = load_workbook(filename=filepath)
    try: sheet = wb['values'] # set worksheet to the values sheet
    except: sheet = wb['Calculation']
    # iterate through each of the equipment and append it to the object
    headers = list()

    """
    Search for header row before finding data
    """
    header_row_location = None 
    for idx, row in enumerate(sheet.iter_rows(values_only=True)):
        #gow through each row in the excel worksheet
        if row[0] == "eqpt_name":
            #start saving the equipment 
            header_row_location = idx  
            for idx, item in enumerate(equipment.items): # each equipment 
                col_number = 1 
                for key, val in item.items():
                    """
                    Equipment {'eqpt_name':['asdf', ' '], '...'}
                    """
                    sheet.cell(row = header_row_location + 1 + idx + 1,
                                column = col_number,
                                value = val[0])
                    col_number +=1
            break  
    # excel file might be open 
    try:
        wb.save(filepath) 
        popup = Popup("File Saved", f"The inputs were saved successfuly to {filepath}")
        popup.alert()
    except:
        popup = Popup("Error", f"Please close {filepath} and save again.") 
        popup.alert()

    


if __name__ == "__main__":
    pass
