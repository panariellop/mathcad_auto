import os, sys
#sys.path.insert(1, os.getcwd() + "\\build\\MathCadPy") #allows inport of mathcad module 
#from mathcadpy import Mathcad, Worksheet #loading custom 
from MathcadPy import Mathcad, Worksheet
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
        self.excel = ""
        self.wall_template = "" 
        self.floor_template = ""
        self.wallfloor_template = ""
        self.ceiling_template = ""
    def display_and_update(self):
        """
        Displays the window and will update the object variables when the user hits continue
        """
        sg.theme("Reddit")
        window = sg.Window("Mathcad Automation", [
            [sg.Frame("Choose Excel File*", [[sg.FileBrowse(key = "excel_file", enable_events = True), sg.InputText(self.excel, key = "excel_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
            [sg.Frame("Choose Database File", [[sg.FileBrowse(key = "database_file", enable_events = True), sg.InputText(self.database, key = "database_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
            
            [sg.Frame("Choose Mathcad Templates*", [
                    [sg.Frame("Choose Wall Mounted Template", [[sg.FileBrowse(key = "wall_template_file", enable_events = True), sg.InputText(self.wall_template, key = "wall_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor Mounted Template", [[sg.FileBrowse(key = "floor_template_file", enable_events = True), sg.InputText(self.floor_template, key = "floor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor and Wall Mounted Template", [[sg.FileBrowse(key = "wallfoor_template_file", enable_events = True), sg.InputText(self.wallfloor_template, key = "wallfloor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Ceiling Mounted Template", [[sg.FileBrowse(key = "ceiling_template_file", enable_events = True), sg.InputText(self.ceiling_template, key = "ceiling_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                ])],

            [sg.Button("Continue", key = "continue", button_color = "green")],
        
        ])
        """Listen for events"""
        while True:
            event, values = window.read()
            if event == 'OK' or event == sg.WIN_CLOSED:
                window.close()
                return False 
            else:
                if event == "continue": #user has input all information 
                    self.database = values['database_name']
                    self.excel = values['excel_name']
                    self.wall_template = values['wall_template_name']
                    self.floor_template = values['floor_template_name']
                    self.wallfloor_template = values['wallfloor_template_name']
                    self.ceiling_template = values['ceiling_template_name']
                    window.close()
                    return


class Popup():
    def __init__(self, title, message):
        self.title = title
        self.message = message
    def confirm(self)->bool:
        popup = sg.Window(self.title, [
                        [sg.Text("")],
                        [sg.Text(self.message), sg.Button("YES", key = "YES", button_color='green'), sg.Button("NO", key = "NO", button_color='red')],
                        [sg.Text("")],
                        ])
        while True:
            event, values = popup.read()
            if event == "OK" or event == "NO" or event == sg.WIN_CLOSED:
                popup.close()
                return False 
            else:
                popup.close()
                return True 
    def alert(self):
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message)],
            [sg.Button("OK", key = 'OK', button_color = 'green')],
        ])
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
        ])
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
        self.save_to_database = True 
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
    """
    filename = filename.split(".")[-1]
    if filename != filetype:
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

    

def load_gui():
    
    files = SelectTemplates()
    files.display_and_update()
    equipment = get_eqpt_from_xl(files.excel) #initial loading of eqpt data 

    sg.theme('Reddit')
    sg.set_options(suppress_raise_key_errors=True, 
        suppress_error_popups=True, suppress_key_guessing=True,
        icon = resource_path("./main_build/images/ma_logo.ico"))
    default_input_size = (14, 1)
    layout = [         
                  
        [  
            sg.Checkbox("Save to database?", key = "database_save", default = True ), 
            sg.Button("Change Input Files", key = "change_input_files")
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
                            sg.Button("Previous", key="previous", size = (8,1)), sg.Button("Next", key = "next", size = (7,1))
                        ],
                    ])],
                ]),
                sg.Column([
                    [sg.Frame("Inputs", 
                        load_inputs(equipment)
                    )],
                ]),
                sg.Column([
                    [sg.Frame("Outputs", 
                        [[sg.Listbox(values = [], 
                                    size = (30, 20),
                                    key = 'outputs',
                                    select_mode = "LISTBOX_SELECT_MODE_BROWSE",
                                    right_click_menu = ['&Right', ["Copy"]],
                                    enable_events = True)]]
                    )],
                    [sg.Button("Preview Calculation Outputs", key = "calculate")], 
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

        [sg.Column([[
            sg.Frame("DETERMINE SEISMIC FORCE", [ #first column
                [sg.Text("F_p"), 
                    sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_output"),
                    ],
                [sg.Text("F_p_max"), 
                    sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_max_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_max_output"),
                    ],
                [sg.Text("F_p_min"), 
                    sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_min_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_min_output"),
                    ],
                [sg.Text("F_p"), 
                    sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_tot_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_tot_output"),
                    ],
            
            ]
            ,size = (100, -1))
            ]]), sg.Column([ #second column
               [sg.Frame("DETERMINE SEISMIC FORCE", [
                    [sg.Text("Connection to equipment"), sg.Combo(["ASD", "LRFD"], enable_events = True, key = "connection_to_eqpt")],
                    [sg.Text("Load Combinations:")], 
                    [sg.Text("F_PV:="), sg.InputText("", key = "f_pv_output", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],
                    [sg.Text("F_PH:="), sg.InputText("", key = "f_ph_output", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],

                   ])], 

            ]), sg.Column([#third column

                [sg.Frame("DETERMINE SEISMIC FORCE", [
                    [sg.Text("Connection to base"), sg.Combo(["ASD", "LRFD"], enable_events = True, key = "connection_to_base")],
                    [sg.Text("Load Combinations:")], 
                    [sg.Text("F_PV:="), sg.InputText("", key = "f_pv_output1", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],
                    [sg.Text("F_PH:="), sg.InputText("", key = "f_ph_output1", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],

                    ])]
                ])],

            [sg.Text("Determine Maximum Tension and Shear at Anchor Points")],
            [sg.Column([
                [sg.Text("Connection to Equiptment", size = (30, 1))], 
                [sg.Text("T_max =", key = "eqpt_t_max_det_label"), sg.InputText("", size = default_input_size, key = "eqpt_t_max_u_determine")],
                [sg.Text("V_max =", key = "eqpt_v_max_det_label"), sg.InputText("", size = default_input_size, key = "eqpt_v_max_u_determine")],
            ]),
            sg.Column([
                [sg.Text("Connection to Base")], 
                [sg.Text("T_max =", key = "base_t_max_det_label"), sg.InputText("", size = default_input_size, key = "base_t_max_u_determine")],
                [sg.Text("V_max =", key = "base_v_max_det_label"), sg.InputText("", size = default_input_size, key = "base_v_max_u_determine")],
            ]),
            ],

        [sg.Text("Status: ", background_color = "yellow"), sg.Text("OK", key = "cur_status", size = (20,1), background_color = "yellow")],
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
                print(equipment.items[equipment.cur_index][event][0])

            """
            Move to the next or previous eqpt  
            """
            if event == "next" or event == "previous":
                if event == "next":
                    equipment.next_index()
                if event == "previous":
                    equipment.prev_index()  
                if files.excel != "" and check_file_type(files.excel, 'xlsx'):
                    for key, val in equipment.items[equipment.cur_index].items():
                        values[key] = val
                        window[key].update(val)
                window['outputs'].update(values = [])
                window['cur_status'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
            """
            Display the eqpt being selected by the listbox (left most column)
            """
            if event == "equipment_list":
                #get the current index 
                equipment.cur_index = window['equipment_list'].get_indexes()[0]
                #update viewport 
                for key, val in equipment.items[equipment.cur_index].items():
                        values[key] = val
                        window[key].update(val)
                window['outputs'].update(values = [])
                window['cur_status'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')     

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
                    values['cur_status'] = "Please select files"
                    window['cur_status'].update("Please select files")
                else:
                    outputs = mathcad_calculate(equipment, files)
                    for key, val in outputs.items():
                        #cleanup
                        val = str(val[0]) + str(val[1])
                        val = val.replace("{", "")
                        val = val.replace("}", "")
                    output_layout = list() #this is where the sg objects live 
                    for key, val in outputs.items():
                        output_layout.append(str(key) + " = " + str(val))
                    window['outputs'].update(values = output_layout)
                alert = Popup("Calcuation Complete", "Output fields have been updated.")
                alert.alert()
                values['cur_status'] = "Output fields updated"
                window['cur_status'].update("Output fields updated")
            






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
        except:
            print("Equipment name, mounting location, and tags must all be included")
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
            print(cur_eqpt)
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
    print(template_file)
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
        if(equipment.save_to_database == True):
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
