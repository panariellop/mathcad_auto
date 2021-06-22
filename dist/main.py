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

def gen_random_string(length:int)->str:
    out = ""
    for i in range(length):
        char = random.randint(65, 90)
        out += chr(char)
    return out 
def check_file_type(filename, filetype):
    filename = filename.split(".")[-1]
    if filename != filetype:
        return False
    return True 
def test_template_exists(template_file:str, mounting_location:str)->bool:
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
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def load_gui():
    sg.theme('Reddit')
    sg.set_options(suppress_raise_key_errors=True, 
        suppress_error_popups=True, suppress_key_guessing=True,
        icon = resource_path("./main_build/images/ma_logo.ico"))
    default_input_size = (14, 1)
    layout = [

        [sg.Column([
            [sg.Frame("Choose Excel File*", [[sg.FileBrowse(key = "excel_file", enable_events = True), sg.InputText(key = "excel_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
        ]),
        sg.Column([
            [sg.Frame("Choose database", [[sg.FileBrowse(key = "database_file", enable_events = True), sg.InputText(key = "database_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
        ]),
        ],

                  
        [   sg.Text("Equipment Name: "), sg.InputText(key = "eqpt_name", size = (30, 1), background_color = "yellow"), 
            sg.Text("Mounting Location: "), sg.Combo(["WALL","CEILING", "FLOOR", "WALL,FLOOR"], enable_events = True, key = "mounting_location"),
            sg.Text("Tags: "), sg.InputText(key = "tags", size = (30, 1)),
            sg.Checkbox("Save to database?", key = "database_save", default = True ), 
        ],

        [
        sg.Text("W_p :="), sg.InputText("", size=(4,1), key = "w_p_input"), sg.Text("lbf", size = (60,1)),
        sg.Button("Preview", key = "calculate"), 
        sg.Text("File Name*"), sg.InputText(key = 'save_file_name', size = (15,1)), sg.Text(".mcdx"),
        sg.Frame("", [[
            sg.Button("Generate Report", key = "generate_report", size = (17,1)), 
        ],
        [
            sg.Button("Previous", key="previous", size = (8,1)), sg.Button("Next", key = "next", size = (7,1))
        ],
        [
            sg.Button("Generate Report For All", key = "generate_report_for_all")
        ],
        ])],

        [sg.Column([
            [sg.Frame("SEISMIC PARAMETERS & GEOMETRY", [

                [sg.Text("S_DS:=", size = (6,1)), sg.InputText(size = default_input_size, key = "s_ds_input")],
                [sg.Text("a_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "a_p_input")],
                [sg.Text("R_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "r_p_input")],
                [sg.Text("I_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "i_p_input")],
                [sg.Text("z:=", size = (6,1)), sg.InputText(size = default_input_size, key = "z_input")],
                [sg.Text("h:=", size = (6,1)), sg.InputText(size = default_input_size, key = "h_input")],
                [sg.Text("z/h:=", size = (6,1)), sg.InputText(size = default_input_size, key = "z_h_output", background_color='yellow', text_color='black')],
                [sg.Text("")],
                [
                    sg.Text("A:=", size = (4,1)), sg.InputText(size = default_input_size, key = "capital_a_input"), sg.Text("in", size = (6,1)), 
                    sg.Text("B:=", size = (4,1)), sg.InputText(size = default_input_size, key = "capital_b_input"), sg.Text("in", size = (6,1))
                ],
                [
                    sg.Text("a:=", size = (4,1)), sg.InputText(size = default_input_size, key = "a_input"), sg.Text("in", size = (6,1)), 
                    sg.Text("b:=", size = (4,1)), sg.InputText(size = default_input_size, key = "b_input"), sg.Text("in", size = (6,1))
                ],
                [sg.Text("H:=", size = (4, 1)), sg.InputText(size = default_input_size, key = "capital_h_input"), sg.Text("in")],
                [sg.Text("")],
                [sg.Text("CG_y:= 2/3 * H =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_y_output", background_color='yellow')], 
                [sg.Text("CG_X1:= A/2 =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_x1_output", background_color='yellow')], 
                [sg.Text("CG_X2:= B/2 =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_x2_output", background_color='yellow')], 


            ]
            , size = (100,-1))]
            ]),


        #(Right hand column )
        sg.Column([
                [sg.Frame("Choose Templates*", [
                    [sg.Frame("Choose Wall Mounted Template", [[sg.FileBrowse(key = "wall_template_file", enable_events = True), sg.InputText(key = "wall_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor Mounted Template", [[sg.FileBrowse(key = "floor_template_file", enable_events = True), sg.InputText(key = "floor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Floor and Wall Mounted Template", [[sg.FileBrowse(key = "wallfoor_template_file", enable_events = True), sg.InputText(key = "wallfloor_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                    [sg.Frame("Choose Ceiling Mounted Template", [[sg.FileBrowse(key = "ceiling_template_file", enable_events = True), sg.InputText(key = "ceiling_template_name", size = (30,1), background_color = 'white', enable_events = True)], ])],
                ])]
            ]),

            ],

        [sg.Column([[
            sg.Frame("DETERMINE SEISMIC FORCE", [ #first column
                [sg.Text("F_p"), 
                    #sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_output"),
                    ],
                [sg.Text("F_p_max"), 
                    #sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_max_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_max_output"),
                    ],
                [sg.Text("F_p_min"), 
                    #sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_min_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_min_output"),
                    ],
                [sg.Text("F_p"), 
                    #sg.Image(filename = (os.getcwd() + "\\main_build\images\\rsz_f_p_tot_equation.png")), 
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
    """Some important values"""
    eqpt_num = 1
    max_rows = 0
    """GUI LOOP"""
    while True: 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
        else:
            """
            Load an excel file 
            Update the current eqpt being viewed 
            """
            if event == "excel_name" or event == "next" or event == "previous":
                if event == "next":
                    eqpt_num = (eqpt_num + 1) % (max_rows+1)
                    if eqpt_num == 0: eqpt_num = 1
                if event == "previous":
                    eqpt_num = (eqpt_num - 1) % (max_rows+1)
                    if eqpt_num == 0: eqpt_num = max_rows  
                if values["excel_name"] != "" and check_file_type(values['excel_name'], 'xlsx'):
                    inputs, num_rows = set_inputs_from_xl(values['excel_name'], eqpt_num)
                    max_rows = num_rows -1 
                    for key,val in inputs.items():
                        values[key] = val
                        window[key].update(val)
                window['cur_status'].update(f'Equipment {eqpt_num}/{max_rows} loaded')
                

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
            Generate report from the values input
            """
            if event == "generate_report": #perform calculations  
                #check if the correct files are input 
                if values['excel_name'] == "" or check_file_type(values['excel_name'], "xlsx") != True:
                    values['cur_status'] = "Please select files"
                    window['cur_status'].update("Please select files")
                if values['save_file_name'] == "":
                    values['cur_status'] = "Please write file name"
                    window['cur_status'].update("Please write file name")
                else:
                    values['cur_status'] = "Generating Report"
                    window['cur_status'].update("Generating Report")

                    if values['mounting_location'] == "WALL":
                        template_file = values['wall_template_name']
                    elif values['mounting_location'] == "FLOOR":
                        template_file = values['floor_template_name']
                    elif values['mounting_location'] == "WALL, FLOOR" or values['mounting_location'] == "WALL,FLOOR":
                        template_file = values['wallfloor_template_name']
                    elif values['mounting_location'] == "CEILING":
                        template_file = values['ceiling_template_name']
                    else:  #defaults to floor mounted 
                        template_file = values['floor_template_name']
                    if test_template_exists(template_file, mounting_location=values['mounting_location'])!=True:
                        alert = Popup("Alert", "Please select a template file corresponding to the mounting location.")
                        alert.alert()
                        continue #template does not exist 
                    status = generate_report(values, template_file, debug = False)
                    if status:
                        alert = Popup("File saved", "The file have been saved successfuly.")
                        alert.alert()
                        status = "File saved."
                    else:
                        status = "Error saving file."
                    values['cur_status'] = status 
                    window['cur_status'].update(status)

            """
            Generate Report for all eqpt
            """
            if event == "generate_report_for_all":
                if values['excel_name'] == "" or values['wall_template_name'] == ""or values['floor_template_name'] == ""or values['wallfloor_template_name'] == ""or values['ceiling_template_name'] == "":
                    values['cur_status'] = "Please select files"
                    window['cur_status'].update("Please select files")
                else:
                    #pre-determine the max number of rows 
                    my_inputs, max_num_rows = set_inputs_from_xl(values['excel_name'], 1)
                    max_rows = max_num_rows - 1 
                    num_wall_templates, num_floor_templates, num_wallfloor_templates, num_ceiling_templates = 1,1,1,1
                    #copy the template file for each 
                    for i in range(1, max_rows+1):
                        if values['mounting_location'] == "WALL":
                            wall_new_name = values['wall_template_name'].split(".")[0] + str(num_wall_templates) + ".mcdx"
                            copyfile(values['wall_template_name'],wall_new_name)
                            num_wall_templates += 1
                        if values['mounting_location'] == "FLOOR":
                            floor_new_name = values['floor_template_name'].split(".")[0] + str(num_floor_templates) + ".mcdx"
                            copyfile(values['floor_template_name'],floor_new_name)
                            num_floor_templates += 1 
                        if values['mounting_location'] == "WALL,FLOOR" or values['mounting_location'] == "WALL, FLOOR" or values['mounting_location'] == "FLOOR,WALL" or values['mounting_location'] == "FLOOR, WALL":
                            wallfloor_new_name = values['wallfloor_template_name'].split(".")[0] + str(num_wallfloor_templates) + ".mcdx"
                            copyfile(values['wallfloor_template_name'],wallfloor_new_name)
                            num_wallfloor_templates += 1
                        if values['mounting_location'] == "CEILING":
                            ceiling_new_name = values['ceiling_template_name'].split(".")[0] + str(num_ceiling_templates) + ".mcdx"
                            copyfile(values['ceiling_template_name'],ceiling_new_name)
                            num_ceiling_templates += 1
                        
                        

                    threads = list()
                    num_threads = 4
                    cur_row = 1
                    while cur_row <= max_rows:
                        for i in range(num_threads):
                            if(cur_row<=max_rows):
                                print(f'Processing equipment: {cur_row}/{max_rows}')
                                new_values = copy.copy(values) # need to copy values to avoid pass by reference 
                                t = threading.Thread(target = pre_generate_report, args = (cur_row, new_values))
                                threads.append(t)
                                t.start()
                                cur_row += 1 
                            else:
                                break
                        for i in range(len(threads)):
                            threads[i].join() #join all threads to the main thread when finished
                    print("Finished threading ...")
                    #cleanup files -- need to wrap in try except continue in case same file is used for multiple templates 
                    for i in range(1,num_wall_templates+1):
                        try:
                            os.remove(values['wall_template_name'].split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                    for i in range(1,num_floor_templates+1):
                        try:
                            os.remove(values['floor_template_name'].split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                    for i in range(1,num_wallfloor_templates+1):
                        try:
                            os.remove(values['wallfloor_template_name'].split(".")[0] + str(i) + ".mcdx")
                        except: continue
                    for i in range(1,num_ceiling_templates+1):
                        try:
                            os.remove(values['ceiling_template_name'].split(".")[0] + str(i) + ".mcdx")
                        except: continue 
                    


                    # for i in range(1, max_rows+1):
                    #     new_name = values['template_file'].split(".")[0] + str(i) + ".mcdx"
                    #     os.remove(new_name)
                alert = Popup("File saved", "The files have been saved successfuly.")
                alert.alert()
                window['cur_status'].update("Reports generated.")


            """
            Get the outputs from the mathcad file
            """
            if event == "calculate":
                if values['excel_name'] == "":
                    values['cur_status'] = "Please select files"
                    window['cur_status'].update("Please select files")
                else:
                    out = mathcad_calculate(values)
                    for key, val in out.items():
                        #cleanup
                        val = str(val[0]) + str(val[1])
                        val = val.replace("{", "")
                        val = val.replace("}", "")
                        if key == "f_pv_output":
                            values['f_pv_output1'] = val
                            window['f_pv_output1'].update(val)
                        elif key == "f_ph_output":
                            values['f_ph_output1'] = val
                            window['f_ph_output1'].update(val)
                        #save
                        values[key] = val
                        window[key].update(val)
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
                values['tags'].upper(), 
                values['eqpt_name'].upper(),
                values['mounting_location'].upper(),
                unique_report_name,
            ]
        except:
            print("Equipment name, mounting location, and tags must all be included")
        csv_writer.writerow(new_row)
    f.close()
    return True 
    # except: 
    #     return False 



def set_inputs_from_xl(filepath: str, eqpt_num:int):
    """
    Gets all the inputs from the excel sheet and returns the proper values packet back 
    """
    inputs = dict()
    wb = load_workbook(filename = filepath)
    sheet = wb['values']
    for i in range(eqpt_num):
        num = str(eqpt_num + 1)
        inputs['eqpt_name'] = sheet['A'+num].value
        inputs['mounting_location'] = sheet['B'+num].value.upper().strip(" ")
        inputs['tags'] = sheet['C'+num].value
        inputs['w_p_input'] = sheet['D' + num].value
        inputs['s_ds_input'] = sheet['E' + num].value
        inputs['a_p_input'] = sheet['F' + num].value
        inputs['r_p_input'] = sheet['G' + num].value
        inputs['i_p_input'] = sheet['H' + num].value
        inputs['z_input'] = sheet['I' + num].value
        inputs['h_input'] = sheet['J' + num].value
        inputs['capital_a_input'] = sheet['K' + num].value
        inputs['capital_b_input'] = sheet['L' + num].value
        inputs['a_input'] = sheet['M' + num].value
        inputs['b_input'] = sheet['N' + num].value
        inputs['capital_h_input'] = sheet['O' + num].value



    
    return inputs, sheet.max_row
     

def mathcad_calculate(values:dict, debug = False):
    """
    Gets all the inputs and performs calculations, 
    returns a dictionary with the output values 
    """
    
    mathcad_app = Mathcad(visible = debug)
    if values['mounting_location'] == "WALL":
        template_file = values['wall_template_name']
    elif values['mounting_location'] == "FLOOR":
        template_file = values['floor_template_name']
    elif values['mounting_location'] == "WALL, FLOOR" or values['mounting_location'] == "WALL,FLOOR":
        template_file = values['wallfloor_template_name']
    elif values['mounting_location'] == "CEILING":
        template_file = values['ceiling_template_name']
    else:  #defaults to floor mounted 
        template_file = values['floor_template_name']
    new_filepath = template_file.split("/")[0:-1] 
    new_filepath = "/".join(new_filepath)
    new_filepath = new_filepath + "/" + "temp" + ".mcdx" 
    if test_template_exists(template_file, mounting_location=values['mounting_location'])!=True:
        alert = Popup("Alert", "Please select a template file corresponding to the mounting location.")
        alert.alert()
        return dict()#template does not exist 
    cur_worksheet = mathcad_app.open(template_file) 

    tosave = dict()
    inputs = [
            'w_p_input', 's_ds_input',
            'a_p_input', 'r_p_input',
            'i_p_input', 'z_input',
            'h_input', 'capital_a_input',
            'capital_b_input', 'a_input',
            'b_input', 'capital_h_input',
    ]
    for i in inputs:
        tosave[i] = values[i]
    for key, value in tosave.items():
        cur_worksheet.set_real_input(str(key), float(value))
    cur_worksheet.ws_object.Synchronize()
    toout = dict()
    outputs = [
            'z_h_output', 'cg_y_output', 
            'cg_x1_output', 'cg_x2_output',
            'cg_x2_output', 'f_p_output',
            'f_p_max_output', 'f_p_min_output',
            'f_p_tot_output', 'f_pv_output',
            'f_ph_output',

    ]
    for o in outputs:
        toout[o] = cur_worksheet.get_real_output(o)
    if debug == False:
        cur_worksheet.close(2) #closes the worksheet and doesn't save it


    return toout


def set_mathcad_inputs(inputs:dict, worksheet:Worksheet)->bool:
    """
    Gets all the inputs as a dictionary 
    returns True if successful, False if unsuccessful
    """
    try:
        for key in inputs:
            worksheet.set_real_input(str(key), inputs[key])
        return True 
    except:
        return False

def pre_generate_report(eqpt_num, values):
    inputs, num_rows = set_inputs_from_xl(values['excel_name'], eqpt_num)
    for key,val in inputs.items():
        values[key] = val
    new_name = values['eqpt_name']
    new_name = new_name.replace(" ", "_")
    new_name += "_report"
    values['save_file_name'] = new_name #passing this to the generate_report function 
    if values['mounting_location'] == "WALL":
        template_file = values['wall_template_name'].split(".")[0] + str(eqpt_num) + ".mcdx" #need this to enable multithreading
    elif values['mounting_location'] == "FLOOR":
        template_file = values['floor_template_name'].split(".")[0] + str(eqpt_num) + ".mcdx"
    elif values['mounting_location'] == "WALL, FLOOR" or values['mounting_location'] == "WALL,FLOOR":
        template_file = values['wallfloor_template_name'].split(".")[0] + str(eqpt_num) + ".mcdx"
    elif values['mounting_location'] == "CEILING":
        template_file = values['ceiling_template_name'].split(".")[0] + str(eqpt_num) + ".mcdx"
    else:  #defaults to floor mounted 
        template_file = values['floor_template_name'].split(".")[0] + str(eqpt_num) + ".mcdx"
    if test_template_exists(template_file, mounting_location=values['mounting_location'])!=True:
        alert = Popup("Alert", "Please select a template file corresponding to the mounting location.")
        alert.alert()
        return #template does not exist 
    status = generate_report(values, template_file, debug = False)
    print(f'Finished generating file {str(status)}')

def generate_report(values, template_file, debug = False)->bool:
    """
    Generates report with input values found in the gui 
    Saves the file in the save folder as the template chosen
    """
    mathcad_app = Mathcad(visible = debug)
    cur_worksheet = mathcad_app.open(template_file) 

    tosave = dict()
    inputs = [ #all the inputs in the mathcad worksheet 
            'w_p_input', 's_ds_input',
            'a_p_input', 'r_p_input',
            'i_p_input', 'z_input',
            'h_input', 'capital_a_input',
            'capital_b_input', 'a_input',
            'b_input', 'capital_h_input',
    ]
    for i in inputs:
        tosave[i] = values[i]
    for key, value in tosave.items():
        try:
            cur_worksheet.set_real_input(str(key), float(value))
        except:
            pass

    #name and mounting location:
    try:
        cur_worksheet.set_string_input('eqpt_name', values['eqpt_name'])
        cur_worksheet.set_string_input('mounting_location', values['mounting_location'])
    except:
        pass

    
    #check if output folder exists, if not, make one 
    output_folder_filepath = os.getcwd() + "/mathcad_automation_output"
    if not os.path.exists(output_folder_filepath):
        os.makedirs(output_folder_filepath)

    unique_string = gen_random_string(8)
    report_filepath = output_folder_filepath + "/" + values['save_file_name'] + "_"+ unique_string+ ".mcdx" 
    

        
    if cur_worksheet.save_as(report_filepath): #save the report 
        cur_worksheet.close()
        #save to reports ledger 
        if(values['database_save'] == True):
            if(values['database_name'] == ""):
                ledger_filepath = output_folder_filepath + "/all_mathcad_reports.csv" #defaults save to the same folder as output if not specified 
            else:
                ledger_filepath = values['database_name']
            save_eqpt_to_csv(values, ledger_filepath, (values['save_file_name'] + "_"+ unique_string+ ".mcdx"))
        return True 
    else:
        cur_worksheet.close()
        return False


if __name__ == "__main__":
    load_gui()
