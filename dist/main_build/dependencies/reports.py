"""
All of the functions that perform report generating or calculations with Mathcad 
"""
from main_build.dependencies.filestream import * 
from main_build.dependencies.data import Equipment
from main_build.dependencies.gui import * 
from main_build.MathcadPy.mathcadpy import Mathcad  # loading custom

# so user can copy to clipboard
# so we can grab images from the sheet

import os 

def mathcad_calculate(eqpt, template_file, debug=False)->dict:
    """
    Gets all the inputs and performs calculations,
    returns a dictionary with the output values
    """
    cur_eqpt = eqpt.items[eqpt.cur_index]
    mathcad_app = Mathcad(visible=debug) #creates a Mathcadpy object
    # Create a new temp file to fill in the values
    new_filepath = template_file.split("/")[0:-1]
    new_filepath = "/".join(new_filepath)
    new_filepath = new_filepath + "/" + "temp" + ".mcdx"
    #some debug print statements
    print("Template file: ", template_file)
    print("Mathcad application: ", mathcad_app, mathcad_app.version, mathcad_app.open_worksheets)
    cur_worksheet = mathcad_app.open(template_file) #open the template file

    for input in eqpt.inputs:  # set inputs
        try:
            cur_worksheet.set_real_input(input, float(cur_eqpt[input][0]), units=cur_eqpt[input][1],
                                         preserve_worksheet_units=False)  # alias, value, units
        except Exception as e:
            print(e)
    cur_worksheet.ws_object.Synchronize()  # must synchronize to make sure outputs are being updated
    toout = dict()
    output_aliases = cur_worksheet.outputs() #get the aliases for each of the worksheet's outputs
    for o in output_aliases:  # assign each alias the value associated with the output ex: r = 12
        toout[o] = cur_worksheet.get_real_output(o) #get the real value of the output
    if debug == False:
        cur_worksheet.close(2)  # closes the worksheet and doesn't save it

    return toout




def pre_generate_report(equipment: Equipment, files, cur_directory, generating_multiple_reports=False):
    """
    Checks if the proper template is given
    Creates a filename or asks for it
    Passes on the equipment (extracts the current eqpt from the object), file name, and template path to the generate report function
    """
    cur_eqpt = equipment.items[equipment.cur_index]
    file_name = str()
    if generating_multiple_reports:  # generates a unique eqpt name (used if generating multiple reports)
        file_name = cur_eqpt['eqpt_name'][0]
        file_name = file_name.replace(" ", "_")
        file_name += "_report_"
        file_name += helpers.gen_random_string(8)
    else:  # prompts user for a filename input
        popup = Popup("File Name", "Choose a file name:")
        file_name = popup.take_input(".mcdx")
        if file_name == "" or file_name == None: return False

    """
    copy files and select template file depending on the mounting location of the cur_eqpt
    """
    """
    if generating_multiple_reports:
        #make a new template file path - we need to make multiple because we don't want the threads to collide
        template_file = files.templates[cur_eqpt['mounting_location'][0]].split(".")[0] + str(
        equipment.cur_index) + ".mcdx"
        #copy the template so we can work on it
        copyfile(files.templates[cur_eqpt['mounting_location'][0]], template_file)
    else:
    """
    template_file = files.templates[cur_eqpt['mounting_location'][0]]

    #call generate report to set inputs and save file
    status = generate_report(cur_eqpt, equipment, file_name, template_file, files, cur_directory, debug=False)
    print(f'Finished generating file {str(status)}')  # some debug output
    return status




def generate_report(cur_eqpt, equipment: Equipment, file_name: str, template_file: str, files, cur_directory, debug=False) -> bool:
    """
    Generates report with input values found in the gui
    Saves the file in the save folder as the template chosen
    """

    mathcad_app = Mathcad(visible=debug)
    cur_worksheet = mathcad_app.open(template_file)

    for input in equipment.inputs:  # set all the real number inputs on the mathcad file
        try:
            cur_worksheet.set_real_input(str(input), float(cur_eqpt[input][0]), units=cur_eqpt[input][1],
                                         preserve_worksheet_units=False)  # alias, value, units
        except:
            pass

    # Set name and mounting location and project number and equipment number on the worksheet :
    for i in ['eqpt_name', 'mounting_location', 'project_number', 'eqpt_number']:
        try:
            cur_worksheet.set_string_input(i, str(cur_eqpt[i][0])) # set the string on the worksheet
        except Exception as e:
            print('Error editing the string field in Mathcad: ', e)

    # check if output folder exists, if not, make one
    output_folder_filepath = cur_directory + "/mathcad_automation_output"
    if not os.path.exists(output_folder_filepath):
        os.makedirs(output_folder_filepath)

    #get the path of the report
    report_filepath = output_folder_filepath + "/" + file_name + ".mcdx"
    
    if not cur_worksheet.save_as(report_filepath):
        # checks if the document is already created or not, if it is, then create another unique name
        report_filepath = report_filepath.split(".")[0] + "1" + ".mcdx"


    if cur_worksheet.save_as(report_filepath):  # save the report
        cur_worksheet.close()
        # save to reports ledger
        if (files.save_to_database == True):
            if (files.database == ""):
                # defaults save to the same folder as output if not specified
                ledger_filepath = output_folder_filepath + "/all_mathcad_reports.csv"  
            else:
                ledger_filepath = files.database
            #save the entry to the csv
            save_eqpt_to_csv(cur_eqpt, ledger_filepath, file_name) 
        return True
    else:
        cur_worksheet.close()
        return False




    
if __name__ == "__main__":
    pass
