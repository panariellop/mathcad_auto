import os, sys
#sys.path.insert(1, os.getcwd() + "\\build\\MathCadPy") #allows inport of mathcad module 
#from mathcadpy import Mathcad, Worksheet #loading custom 
from MathcadPy import Mathcad, Worksheet
from images import * 
import PySimpleGUI as sg
from pathlib import Path, PurePath
from openpyxl import Workbook as xlwkbk
from openpyxl import load_workbook 
from shutil import copyfile
import threading 
import csv 
import random 
import copy 
from datetime import  date 
from time import sleep 

class SelectTemplates():
    
    def __init__(self):
        self.database = ""
        self.save_to_database = True 
        self.excel = ""
        self.wall_template = "" 
        self.floor_template = ""
        self.wallfloor_template = ""
        self.ceiling_template = ""
        self.images = dict()
    def display_and_update(self):
        """
        Displays the window and will update the object variables when the user hits continue
        """
        sg.theme("Reddit")
        window = sg.Window("Mathcad Automation", [
            [sg.Frame("Choose Excel File*", [[sg.FileBrowse(key = "excel_file", enable_events = True), sg.InputText(self.excel, key = "excel_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
            [sg.Frame("Choose Database File", [[sg.FileBrowse(key = "database_file", enable_events = True), sg.InputText(self.database, key = "database_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
            [sg.Checkbox("Save to database?", key = "save_to_database", default = self.save_to_database)], 
            
            [sg.Frame("Choose Mathcad Templates*", [
                    [sg.Frame("Choose Wall Mounted Template", [[sg.FileBrowse(key = "wall_template_file", enable_events = True), sg.InputText(self.wall_template, key = "wall_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor Mounted Template", [[sg.FileBrowse(key = "floor_template_file", enable_events = True), sg.InputText(self.floor_template, key = "floor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor and Wall Mounted Template", [[sg.FileBrowse(key = "wallfoor_template_file", enable_events = True), sg.InputText(self.wallfloor_template, key = "wallfloor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Ceiling Mounted Template", [[sg.FileBrowse(key = "ceiling_template_file", enable_events = True), sg.InputText(self.ceiling_template, key = "ceiling_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                ])],

            [sg.Button("Continue", key = "continue", button_color = "green")],
        
        ], icon = ma_logo_png)
        """Listen for events"""
        while True:
            event, values = window.read()
            if event == 'OK' or event == sg.WIN_CLOSED:
                window.close()
                return False 
            else:
                if event == "continue": #user has input all information 
                    #error 
                    errors = list()
                    #validate the filepaths 
                    self.save_to_database = values['save_to_database']
                    if check_file_type(values['database_name'], 'csv') or values['database_name'] == "":
                        self.database = values['database_name']
                    else:
                        errors.append("Database file must be a .csv file.")
                    if check_file_type(values['excel_name'], 'xlsx'):
                        self.excel = values['excel_name']
                    else:
                        errors.append("Excel file must be a .xlsx file.")
                    if check_file_type(values['wall_template_name'], "mcdx") or values['wall_template_name'] == "":
                        self.wall_template = values['wall_template_name']
                    else:
                        errors.append("Wall template file must be a .mcdx file.")
                    if check_file_type(values['floor_template_name'], "mcdx") or values['floor_template_name'] == "":
                        self.floor_template = values['floor_template_name']
                    else:
                        errors.append("Floor template must be a .mcdx file.")
                    if check_file_type(values['wallfloor_template_name'], "mcdx") or values['wallfloor_template_name'] == "":
                        self.wallfloor_template = values['wallfloor_template_name']
                    else:
                        errors.append("Wall and Floor template must be a .mcdx file.")
                    if check_file_type(values['ceiling_template_name'], "mcdx") or values['ceiling_template_name'] == "":
                        self.ceiling_template = values['ceiling_template_name']
                    else:
                        errors.append("Ceiling template must be a .mcdx file.")
                    #Error handling 
                    if len(errors) == 0:
                        window.close()
                        return
                    else:
                        alert = Popup("Errors", "\n".join(errors))
                        alert.alert()
                        continue 
    def get_images_from_xl(self, num_images:int):
        """
        Gets all the preview images from the excel file and saves a dictionary of mounting locations and binary images in self.images 
        <num_images:int> Corresponds to the number of mounting locations, indicated in the preview_images portion of the input excel document
        """
        wb = load_workbook(self.excel)
        sheet = wb['preview_images']
        from openpyxl_image_loader import SheetImageLoader 
        image_loader = SheetImageLoader(sheet)
        for i in range(num_images):
            #hard coded 
            mounting_locations = ['wall', 'floor', 'wall,floor', 'ceiling']
            try: #load all the images in cells B2-5 
                image = image_loader.get('B' + str(i+2))
                import io
                buf = io.BytesIO()
                image.save(buf, format="PNG") #save as a bytes string so pysimplegui can use it
                self.images[mounting_locations[i]] =  buf.getvalue()
            except Exception as e:
                print(e)
        



class Popup():
    def __init__(self, title, message):
        self.title = title
        self.message = message
    def confirm(self)->bool:
        popup = sg.Window(self.title, [
                        [sg.Text("")],
                        [sg.Text(self.message), ],
                        [sg.Text("")],
                        [sg.Button("YES", key = "YES", button_color='green'), sg.Button("NO", key = "NO", button_color='red')],
                        ], 
                        icon = ma_logo_png,)
        while True:
            event, values = popup.read()
            if event == "OK" or event == "NO" or event == sg.WIN_CLOSED:
                popup.close()
                return False 
            if event == "YES":
                popup.close()
                return True 
    def alert(self):
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message)],
            [sg.Button("OK", key = 'OK', button_color = 'green')],
        ], 
        icon = ma_logo_png,)
        while True:
            event, values = popup.read()
            if event == "OK" or event == sg.WIN_CLOSED:
                popup.close()
                break 
            else:
                pass 
    def take_input(self, trailing_text:str)->str:
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message), sg.InputText(key = "input", size = (15, 1)), sg.Text(trailing_text)],
            [sg.Button("OK", key = 'OK', button_color = 'green')],
        ], 
        icon = ma_logo_png,)
        while True:
            event, values = popup.read()
            if event == "OK" or event == sg.WIN_CLOSED:
                popup.close()
                return values['input']

class Equipment():
    """
    Class of equipment (list of dictionaries)
    """
    def __init__(self):
        self.items = list()
        self.cur_index = 0 
        self.length = 0 
        self.fields = list()
        self.names = list()
        self.inputs = list()
    def append(self, to_append:dict):
        self.items.append(to_append)
        for key, field in to_append.items(): #key value pair  
            if key not in self.fields: #append fields - this is the first row in the excel document 
                self.fields.append(key)
            if key  == 'eqpt_name' or key == "Equipment Name": #append names of equiptment (always the first column in the template file)
                self.names.append(field[0])
            if key.split("_")[-1] == "input" and key not in self.inputs:
                self.inputs.append(key)
        return 
    def next_index(self): #don't want to throw out of bounds error ! 
        self.cur_index = (self.cur_index + 1) % len(self.items)
    def prev_index(self):
        if self.cur_index == 0:
            self.cur_index = len(self.items) - 1
        else: 
            self.cur_index -= 1

class Outputs():
    def __init__(self):
        self.items = list()
        """
        ['f_p_max_output', [408.81554560308007, 'kg', 0]]
        ['f_p_min_output', [76.65291480057748, 'kg', 0]]
        ['f_p_tot_output', [76.65291480057748, 'kg', 0]]
        """
    def append(self, to_append):
        name = to_append[0]
        values =  list(to_append[1]) #need to convert from tuple to array bc tuple is immutable 
        self.items.append([name, values])
    def clear(self):
        self.items = []
    def display(self)->list:
        to_display = list()
        for i in self.items:
            to_display.append(str(i[0]) + " = " + str(round(i[1][0], 2)) + " " + str(i[1][1])) #name = value units
        return to_display 
    def convert_units(self, in_units, tg_units):
        """
        Convert units: <input> is 'imperial' or 'metric' ; <target> is 'imperial' or 'metric'
        """
        for i in self.items:
            if in_units == "imperial" and tg_units == 'metric': #convert from imperial to metric 
                if i[1][1] == "in":
                    i[1][1] = "m"
                    i[1][0] = convert_units(i[1][0], "in", "m")
                if i[1][1] == "ft":
                    i[1][1] = "m"
                    i[1][0] = convert_units(i[1][0], "ft", "m")
                if i[1][1] == "lb":
                    i[1][1] = "kg"
                    i[1][0] = convert_units(i[1][0], "lb", "kg")
                if i[1][1] == "lbf":
                    i[1][1] = "n"
                    i[1][0] = convert_units(i[1][0], "lb", "n")
            else:
                if i[1][1] == "m":
                    i[1][1] = "ft"
                    i[1][0] = convert_units(i[1][0], "m", "ft")
                if i[1][1] == "kg":
                    i[1][1] = "lb"
                    i[1][0] = convert_units(i[1][0], "kg", "lb")
                if i[1][1] == "n":
                    i[1][1] = "lbf"
                    i[1][0] = convert_units(i[1][0], "n", "lbf")

    


def convert_units(value:int, input_units:str, target_units:str)->int:
    """
    Takes in a value and its units and outputs the value in the target units 
    Supported conversions: m <-> in ; m <-> ft ; kg <-> lb ; n <-> lbf
    """
    input_units = input_units.lower()
    target_units = target_units.lower()
    if input_units == "m" and target_units == "in":
        return value * 39.37008
    elif input_units == "in" and target_units == "m":
        return value / 39.37008
    elif input_units == "m" and target_units == "ft":
        return value * 3.28084
    elif input_units == "ft" and target_units == "m":
        return value / 3.28084
    elif input_units == "kg" and target_units == "lb":
        return value * 2.204623
    elif input_units == "lb" and target_units == "kg":
        return value / 2.204623
    elif input_units == "n" and target_units == "lbf":
        return value * 0.2248089
    elif input_units == "lbf" and target_units == "n":
        return value / 0.2248089

    else: return value 

def gen_random_string(length:int)->str:
    """
    Generates a string of random characters 
    """
    out = ""
    for i in range(length):
        char = random.randint(65, 90)
        out += chr(char)
    return out 
def check_file_type(filename, filetype):
    """
    Checks if the input file is of a certain type
    ex <filename.csv> <csv>
    """
    type = filename.split(".")[-1]
    if type != filetype:
        return False
    return True 
def test_template_exists(template_file:str, mounting_location:str)->bool:
    """
    Tests if a template exists for a given mounting location 
    """
    if mounting_location == "WALL" and template_file != "":
        return True 
    elif mounting_location == "FLOOR" and template_file != "":
        return True 
    elif mounting_location == "FLOOR,WALL" and template_file != "":
        return True 
    elif mounting_location == "FLOOR, WALL" and template_file != "":
        return True 
    elif mounting_location == "WALL, FLOOR" and template_file != "":
        return True 
    elif mounting_location == "WALL,FLOOR" and template_file != "":
        return True 
    elif mounting_location == "CEILING" and template_file != "":
        return True 
    else:
        return False 


def resource_path(relative_path):
    """
    Determines the resource path for an graphic, etc
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_inputs(equipment:Equipment):
    """
    Takes in the equipment and returns all the input fields with sg parts
    """
    input_fields = list()

    for field, value in equipment.items[equipment.cur_index].items(): #each eqpt is a dictionary, field is key 
        name = field.split("(")[0]
        name = name.replace(" ", "")

        input_fields.append(
            [sg.Text(str(name + " = "), size = (20,1)), 
            sg.InputText(value[0], size = (20, 1), key = str(field), enable_events = True), 
            sg.Text(value[1])]
        )
    return input_fields

def update_inputs(equipment:Equipment, values, window):
    """
    Updates the window and value to reflect the object selected 
    """
    for field, val in equipment.items[equipment.cur_index].items():
        values[field] =  val[0]
        window[field].update(val[0])

    return values, window 
    

def load_gui():
    
    files = SelectTemplates()
    files.display_and_update()
    files.get_images_from_xl(num_images = 4)
    equipment = get_eqpt_from_xl(files.excel) #initial loading of eqpt data 
    outputs = Outputs() # preview output object 

    sg.theme('Reddit')
    sg.set_options(suppress_raise_key_errors=True, 
        suppress_error_popups=True, suppress_key_guessing=True,
        icon = ma_logo_png)
    default_input_size = (14, 1)
    layout = [         
                  
        [  
            sg.Button("Change Input Files", key = "change_input_files"), 
            sg.Text(" ", size = (5,1)),
            sg.Button("Refresh", key = "refresh_input_files")
        ],

        

        [
            #list of equiptment
                sg.Column([
                    [sg.Frame("Choose Equipment", [
                        [sg.Listbox(values = equipment.names, 
                                    size = (30, 20),
                                    key = 'equipment_list',
                                    select_mode = "LISTBOX_SELECT_MODE_SINGLE",
                                    enable_events = True,
                        )],
                        [
                            sg.Button("Previous", key="previous", size = (8,1)), 
                            sg.Button("Next", key = "next", size = (7,1)),
                            sg.Text(" ", size = (5,1)),
                            sg.Text("Go to:"),
                            sg.InputText(equipment.cur_index, key = "goto_eqpt", enable_events = True, size = (3, 1)),
                        ],
                        [sg.Text("Equipment: ", key = "cur_eqpt", size = (20,1), background_color = "gray")],
                    ])],
                ]),
                sg.Column([
                    [sg.Frame("Inputs", 
                        load_inputs(equipment)
                    )],
                ]),
                sg.Column([
                    [sg.Frame("Outputs", 
                        [   
                            [sg.Radio("Imperial Units", "RADIO1",  key = "convert_to_imperial", enable_events = True), sg.Radio("Metric Units", "RADIO1", default = True, key = "convert_to_metric", enable_events = True)],

                            [sg.Listbox(values = [], 
                                    size = (30, 20),
                                    key = 'outputs',
                                    select_mode = "LISTBOX_SELECT_MODE_BROWSE",
                                    right_click_menu = ['&Right', ["Copy"]],
                                    enable_events = True)],
                            [sg.Button("Preview Calculation Outputs", key = "calculate")],
                        ],
                        
                    )],
                     
                ])
                

        ],

        [
        
        sg.Frame("", [[
            sg.Button("Generate Report", key = "generate_report", size = (17,1)), 
        ],
        
        [
            sg.Button("Generate Report For All", key = "generate_report_for_all")
        ],
        ])],

        [[sg.Text("Preview Images:")] , [sg.Image(key = "preview_image", data = files.images['wall,floor'])]]
    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)

    """GUI LOOP"""
    while True: 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
        else:
            """
            Change Input Files 
            """
            if event == "change_input_files":
                files.display_and_update()

            """
            Refresh input files
            """
            if event == "refresh_input_files":
                confirm = Popup("Confirm", "This will reload the information from the input excel document and erase any changes you have made to the inputs.")
                if confirm.confirm():
                    equipment = get_eqpt_from_xl(files.excel)
                    files.get_images_from_xl(4)
                    values, window = update_inputs(equipment, values, window)

            
            """
            If user wants to copy output
            """
            if event == "outputs":
                to_copy = window['outputs'].get()[0]
                import pyperclip
                pyperclip.copy(str(to_copy))

            """
            Update the Equipment object when the user edits an input field 
            """
            if event in equipment.fields:
                #change the cur eqpt field being edited 
                equipment.items[equipment.cur_index][event][0] = values[event] 

            """
            Move to the next or previous eqpt  
            """
            if event == "next" or event == "previous":
                if event == "next":
                    equipment.next_index()
                if event == "previous":
                    equipment.prev_index()  
                if files.excel != "" and check_file_type(files.excel, 'xlsx'):
                    values, window = update_inputs(equipment, values, window)
                window['outputs'].update(values = [])
                window['equipment_list'].set_focus(equipment.cur_index) #display the current one being selected 
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                image = files.images[str(equipment.items[equipment.cur_index]['mounting_location'][0]).lower().replace(" ", "")]
                window['preview_image'].update(data = image)
            """
            Display the eqpt being selected by the listbox (left most column)
            """
            if event == "equipment_list":
                #get the current index 
                equipment.cur_index = window['equipment_list'].get_indexes()[0]
                #update viewport
                values, window = update_inputs(equipment, values, window)
                window['outputs'].update(values = [])
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                image = files.images[str(equipment.items[equipment.cur_index]['mounting_location'][0]).lower().replace(" ", "")]
                window['preview_image'].update(data = image)     

            """
            Go to a specific eqpt number 
            """
            if event == "goto_eqpt":
                if values['goto_eqpt'] != "" and int(values['goto_eqpt'])<=len(equipment.items):
                    equipment.cur_index = int(values['goto_eqpt']) - 1 
                    values, window = update_inputs(equipment, values, window) #update the inputs in the window 
                    window['equipment_list'].set_focus(equipment.cur_index) #display the eqpt being selected
                    window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                    image = files.images[str(equipment.items[equipment.cur_index]['mounting_location'][0]).lower().replace(" ", "")]
                    window['preview_image'].update(data = image)
            """
            Update the maximum tension and shear anchor points labels
            """
            if event == "connection_to_base" or event == "connection_to_eqpt":
                if values["connection_to_base"] == "ASD":
                    window['base_t_max_det_label'].update("T_max=")
                    window['base_v_max_det_label'].update("V_max=")
                if values["connection_to_eqpt"] == "ASD":
                    window['eqpt_t_max_det_label'].update("T_max=")
                    window['eqpt_v_max_det_label'].update("V_max=")
                if values["connection_to_base"] == "LRFD":
                    window['base_t_max_det_label'].update("T_u=")
                    window['base_v_max_det_label'].update("V_u=")
                if values["connection_to_eqpt"] == "LRFD":
                    window['eqpt_t_max_det_label'].update("T_u=")
                    window['eqpt_v_max_det_label'].update("V_u=")


            """
            Generate report for one eqpt 
            """
            if event == "generate_report": 
                #check if the correct files are corrrect input 
                if files.excel == "" or check_file_type(files.excel, "xlsx") != True:
                    popup = Popup("Error", "Please select an input excel file.")
                    popup.alert()
                else:
                    status = pre_generate_report(equipment = equipment, files = files, generating_multiple_reports=False)
                    if status:
                        alert = Popup("File saved", "The file have been saved successfuly.")
                        alert.alert()
                    else:
                        alert = Popup("Error", "There was an error saving the file")
                        alert.alert()

            """
            Generate Report for all eqpt
            """
            if event == "generate_report_for_all":
                if files.excel == "" or files.wall_template == ""or files.floor_template == ""or files.wallfloor_template == ""or files.ceiling_template == "":
                    alert = Popup("Alert", "Please select templates for each mounting location")
                    alert.alert()
                else:
                    """
                    Using multithreading to improve speed
                    """
                    threads = list()
                    num_threads = 4
                    cur_row = 0
                    equipment.cur_index = 0 #set to beginning of list 
                    while cur_row < len(equipment.items):
                        for i in range(num_threads):
                            if(cur_row<len(equipment.items)):
                                print(f'Processing equipment: {cur_row+1}/{len(equipment.items)}')
                                t = threading.Thread(target = pre_generate_report, args = (equipment, files, True))
                                threads.append(t)
                                t.start()
                                cur_row += 1 
                                equipment.next_index()
                            else:
                                break 
                        for i in range(len(threads)):
                            threads[i].join() #join all threads to the main thread when finished
                    print("Finished threading ...")
                    #cleanup files -- need to guess the file names (performance should be fine for <1000 pieces of equipment)
                    for i in range(len(equipment.items)):
                        try:
                            os.remove(files.wall_template.split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                    for i in range(len(equipment.items)):
                        try:
                            os.remove(files.floor_template.split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                    for i in range(len(equipment.items)):
                        try:
                            os.remove(files.wallfloor_template.split(".")[0] + str(i) + ".mcdx")
                        except: continue
                    for i in range(len(equipment.items)):
                        try:
                            os.remove(files.ceiling_template.split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                alert = Popup("File saved", "All files have been saved successfuly.")
                alert.alert()


            """
            Preview 
            """
            if event == "calculate":
                if files.excel == "":
                    alert = Popup("Error", "Please select an input excel file from the input files window.")
                    alert.alert()
                else:
                    to_out = mathcad_calculate(equipment, files)
                    outputs.clear()
                    for key, val in to_out.items(): outputs.append([key,val])
                    window['outputs'].update(values = outputs.display())
                    alert = Popup("Calcuation Complete", "Output fields have been updated.")
                    alert.alert()
            if event == "convert_to_imperial":
                outputs.convert_units('metric', 'imperial')
                window['outputs'].update(values = outputs.display())
            if event == "convert_to_metric":
                outputs.convert_units('imperial', 'metric')
                window['outputs'].update(values = outputs.display())
            






    window.close(); del window
    return 

def save_eqpt_to_csv(values, filepath, unique_report_name):
    cur_date = date.today()
    header = False 
    # try:
    try:
        with open(filepath, "r", newline = "") as f:
            pass
    except Exception as e:
        header = True 
    try:
        import stat
        os.chmod(filepath, stat.S_IRWXO)
    except Exception as e:
        print(e)
        pass 
    with open(filepath, "a", newline = "") as f:
        csv_writer = csv.writer(f)
        if header: csv_writer.writerow(["Date","Tags", "Name", "Mounting Location", "File Name"])
        try:
            new_row = [
                cur_date, 
                values['tags'][0].upper(), 
                values['eqpt_name'][0].upper(),
                values['mounting_location'][0].upper(),
                unique_report_name + ".mcdx",
            ]
        except Exception as e:
            print(e)
        csv_writer.writerow(new_row)
    f.close()
    return True 
    # except: 
    #     return False 


def get_eqpt_from_xl(filepath:str)->Equipment:
    """
    Gets all the equipment from an excel file and returns an equipment object 
    """
    wb = load_workbook(filename = filepath)
    sheet = wb['values']
    #iterate through each of the equipment and append it to the object 
    headers = list()
    equipment = Equipment()

    for idx, row in enumerate(sheet.iter_rows(values_only=True)):
        if idx == 0: #header row 
            headers = list(row)
        else:
            cur_eqpt = dict()
            for i, header in enumerate(headers):
                #populates each eqpt with the input fields and [value, units]
                try:
                    units = header.split("(")[1]
                    units = units.strip(")")
                    field = header.split("(")[0]
                    field = field.strip(" ")
                    cur_eqpt[field] = [row[i], units]
                except:
                    cur_eqpt[header] = [row[i], ""] #<- blank units 
            equipment.append(cur_eqpt)
    return equipment

     

def mathcad_calculate(eqpt, files, debug = False):
    """
    Gets all the inputs and performs calculations, 
    returns a dictionary with the output values 
    """
    cur_eqpt = eqpt.items[eqpt.cur_index]
    mathcad_app = Mathcad(visible = debug)
    if cur_eqpt['mounting_location'][0].upper() == "WALL":
        template_file = files.wall_template
    elif cur_eqpt['mounting_location'][0].upper() == "FLOOR":
        template_file = files.floor_template
    elif cur_eqpt['mounting_location'][0].upper() == "WALL, FLOOR" or cur_eqpt['mounting_location'][0].upper() == "WALL,FLOOR":
        template_file = files.wallfloor_template
    elif cur_eqpt['mounting_location'][0].upper() == "CEILING":
        template_file = files.ceiling_template
    else:  #defaults to floor mounted 
        template_file = files.floor_template
    new_filepath = template_file.split("/")[0:-1] 
    new_filepath = "/".join(new_filepath)
    new_filepath = new_filepath + "/" + "temp" + ".mcdx" 
    if test_template_exists(template_file, mounting_location=cur_eqpt['mounting_location'][0].upper())!=True:
        alert = Popup("Alert", "Please select a template file corresponding to the mounting location.")
        alert.alert()
        return dict()#template does not exist 
    cur_worksheet = mathcad_app.open(template_file) 

    for input in eqpt.inputs: #set inputs 
        try:
            cur_worksheet.set_real_input(input, float(cur_eqpt[input][0]), units = cur_eqpt[input][1], preserve_worksheet_units= False) #alias, value, units 
        except Exception as e:
            print(e)
    cur_worksheet.ws_object.Synchronize()
    toout = dict()
    output_aliases = cur_worksheet.outputs()
    for o in output_aliases: #assign each alias the value associated with the output ex: r = 12 
        toout[o] = cur_worksheet.get_real_output(o)
    if debug == False:
        cur_worksheet.close(2) #closes the worksheet and doesn't save it


    return toout


def pre_generate_report(equipment:Equipment, files, generating_multiple_reports = False):
    """
    Checks if the proper template is given 
    Creates a filename or asks for it 
    Passes on the equipment (extracts the current eqpt from the object), file name, and template path to the generate report function
    """
    cur_eqpt = equipment.items[equipment.cur_index]
    file_name = str()
    if generating_multiple_reports: #generates a unique eqpt name (used if generating multiple reports)
        file_name = cur_eqpt['eqpt_name'][0]
        file_name = file_name.replace(" ", "_")
        file_name += "_report_"
        file_name += gen_random_string(8)
    else: #prompts user for a filename input 
        popup = Popup("File Name", "Choose a file name:")
        file_name = popup.take_input(".mcdx")

    if cur_eqpt['mounting_location'][0].upper() == "WALL":
        if generating_multiple_reports:
            template_file = files.wall_template.split(".")[0] + str(equipment.cur_index) + ".mcdx" #need this to enable multithreading
            copyfile(files.wall_template, template_file) #need to copy file to prevent collisions in writing/reading 
        else:
            template_file = files.wall_template

    elif cur_eqpt['mounting_location'][0].upper() == "FLOOR":
        if generating_multiple_reports:
            template_file = files.floor_template.split(".")[0] + str(equipment.cur_index) + ".mcdx"
            copyfile(files.wall_template, template_file)
        else:
            template_file = files.floor_template

    elif cur_eqpt['mounting_location'][0].upper() == "WALL, FLOOR" or cur_eqpt['mounting_location'][0].upper() == "WALL,FLOOR" or cur_eqpt['mounting_location'][0].upper() == "FLOOR, WALL" or cur_eqpt['mounting_location'][0].upper() == "FLOOR,WALL":
        if generating_multiple_reports:
            template_file = files.wallfloor_template.split(".")[0] + str(equipment.cur_index) + ".mcdx"
            copyfile(files.wall_template, template_file)
        else:
            template_file = files.wallfloor_template

    elif cur_eqpt['mounting_location'][0].upper() == "CEILING":
        if generating_multiple_reports: 
            template_file = files.ceiling_template.split(".")[0] + str(equipment.cur_index) + ".mcdx"
            copyfile(files.wall_template, template_file)
        else:
            template_file = files.ceiling_template
    else:  #defaults to floor mounted 
        if generating_multiple_reports:
            template_file = files.floor_template.split(".")[0] + str(equipment.cur_index) + ".mcdx"
            copyfile(files.wall_template, template_file)
        else:
            template_file = files.floor_template
    
    #check to see if the template exists 
    if test_template_exists(template_file, mounting_location=cur_eqpt['mounting_location'][0].upper())!=True:
        alert = Popup("Alert", "Please select a template file corresponding to the mounting location.")
        alert.alert()
        return #template does not exist 

    status = generate_report(equipment, file_name, template_file, files, debug = False)
    print(f'Finished generating file {str(status)}') #some debug output 
    return status 

def generate_report(equipment:Equipment, file_name:str, template_file:str, files, debug = False)->bool:
    """
    Generates report with input values found in the gui 
    Saves the file in the save folder as the template chosen
    """
    mathcad_app = Mathcad(visible = debug)
    cur_worksheet = mathcad_app.open(template_file) 
    cur_eqpt = equipment.items[equipment.cur_index]

    for input in equipment.inputs: #set all the real number inputs on the mathcad file
        try:
            cur_worksheet.set_real_input(str(input), float(cur_eqpt[input][0]), units = cur_eqpt[input][1], preserve_worksheet_units= False) #alias, value, units 
        except:
            pass

    #name and mounting location:
    try:
        cur_worksheet.set_string_input('eqpt_name', cur_eqpt['eqpt_name'])
        cur_worksheet.set_string_input('mounting_location', cur_eqpt['mounting_location'][0])
    except:
        pass

    
    #check if output folder exists, if not, make one 
    output_folder_filepath = os.getcwd() + "/mathcad_automation_output"
    if not os.path.exists(output_folder_filepath):
        os.makedirs(output_folder_filepath)

    report_filepath = output_folder_filepath + "/" + file_name + ".mcdx"
        
    if cur_worksheet.save_as(report_filepath): #save the report 
        cur_worksheet.close()
        #save to reports ledger 
        if(files.save_to_database == True):
            if(files.database == ""):
                ledger_filepath = output_folder_filepath + "/all_mathcad_reports.csv" #defaults save to the same folder as output if not specified 
            else:
                ledger_filepath = files.database
            save_eqpt_to_csv(cur_eqpt, ledger_filepath, file_name)
        return True 
    else:
        cur_worksheet.close()
        return False


if __name__ == "__main__":
    load_gui()
