import os, sys
sys.path.insert(1, os.getcwd() + "\\build\\MathCadPy") #allows inport of mathcad module 
from mathcadpy import Mathcad, Worksheet #loading custom 
# from MathcadPy import Mathcad, Worksheet
import PySimpleGUI as sg
from pathlib import Path, PurePath
from openpyxl import Workbook, load_workbook

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
 

def load_gui():
    sg.theme('Reddit')
    default_input_size = (6, 1)
    layout = [
        [sg.Text("Mounting Location: "), sg.Combo(["WALL","CEILING", "FLOOR", "FLOOR+WALL"], key = "mounting_location")],

        [
        sg.Text("W_p :="), sg.InputText("", size=(4,1)), sg.Text("lbf", size = (60,1)),
        sg.Button("Update", key = "update"), 
        sg.Frame("", [[
            sg.Button("Generate Report", key = "generate_report"), 
        ],
        [
            sg.Button("Previous", key="previous"), sg.Button("Next", key = "next")
        ]
        ])],

        [
            sg.Frame("SEISMIC PARAMETERS & GEOMETRY", [

                [sg.Text("S_DS:=", size = (6,1)), sg.InputText(size = default_input_size, key = "s_ds_input")],
                [sg.Text("a_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "a_p_input")],
                [sg.Text("R_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "r_p_input")],
                [sg.Text("I_p:=", size = (6,1)), sg.InputText(size = default_input_size, key = "i_p_input")],
                [sg.Text("z:=", size = (6,1)), sg.InputText(size = default_input_size, key = "z_input")],
                [sg.Text("h:=", size = (6,1)), sg.InputText(size = default_input_size, key = "h_input")],
                [sg.Text("z/h:=", size = (6,1)), sg.Text(size = default_input_size, key = "z_h_output", background_color='yellow', text_color='black')],
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
                [sg.Text("CG_y:= 2/3 * H =", size = (15, 1)), sg.Text(size = default_input_size, key = "cg_y_ouput", background_color='yellow')], 
                [sg.Text("CG_X1:= A/2 =", size = (15, 1)), sg.Text(size = default_input_size, key = "cg_x1_ouput", background_color='yellow')], 
                [sg.Text("CG_X2:= B/2 =", size = (15, 1)), sg.Text(size = default_input_size, key = "cg_x2_ouput", background_color='yellow')], 


            ]
            , size = (100,-1))
        ],

        [
            sg.Frame("DETERMINE SEISMIC FORCE", [
                [sg.Image(filename = (os.getcwd() + "\\build\images\\f_p_equation.png"))]
            ]
            ,size = (100, -1))
        ],

        [sg.Frame("Choose Excel File", [[sg.FileBrowse(key = "-EXCEL_FILE-"), sg.Text(key = "-EXCEL_NAME-", size = (50,1), background_color = 'white')], [sg.Button("Ok", key = "-OKEXCEL-")]])],
        [sg.Text("")],
        [sg.Frame("Choose template", [[sg.FileBrowse(key = "-TEMPLATE_FILE-"), sg.Text(key = "-TEMPLATE_NAME-", size = (50,1), background_color = 'white')], [sg.Button("Ok", key = "-OKFILE-")]])],
        [sg.Text("")],
        [sg.Text("File Name"), sg.InputText(key = '-SAVEFILENAME-', size = (15,1)), sg.Text(".mcdx")],
        [sg.Text(key = "cur_status", size = (20,3))],
        [sg.Button('Clear Inputs', key = '-CLEAR-')],
    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)
    while True: #gui loop 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
        else:
            if event == "-CLEAR-":
                #creates confirming popup and then clears values
                popup = Popup("Confirm clear", "Are you sure you want to clear all inputs?")
                if popup.confirm() == True:
                    inputs = ["-IN1-", "-IN2-","-IN3-","-IN4-"]
                    for key in inputs:
                        window[key].update("")
                        values[key] = "" 
            elif event == "-TEMPLATE_FILE-":
                window['-TEMPLATE_NAME-'].update(values['-TEMPLATE_FILE-'].split("/")[-1])
            elif event == "generate_report": #perform calculations  
                status = generate_report(values, debug = False)
                if status:
                    status = "File saved."
                else:
                    status = "Error saving file."
                values['cur_status'] = status 
                window['cur_status'].update(status)




    window.close()
    return 

# def excel_to_arr(filepath:str, bounds:list)->list:
#     """
#     bounds define the box which holds data(including header row)

#     Eqpt Name | Weight | COG ...
#     ----------------------------
#     Sink      | 250kg  | 12in

#     header row is defined as the first index of the ouput array 
#     """
#     wb = load_workbook(filepath)


def generate_report(values, debug = False)->bool:
    new_filepath = values['-TEMPLATE_FILE-'].split("/")[0:-1] 
    new_filepath = "/".join(new_filepath)
    new_filepath = new_filepath + "/" + values['-SAVEFILENAME-'] + ".mcdx" 
    mathcad_app = Mathcad(visible = debug)
    cur_worksheet = mathcad_app.open(values['-TEMPLATE_FILE-']) 
    #TODO make sure value input matches template input 
    cur_worksheet.set_real_input('a', 18)
    if cur_worksheet.save_as(new_filepath):
        cur_worksheet.close()
        return True 
    else:
        cur_worksheet.close()
        return False


if __name__ == "__main__":
    #generate_file(debug = True)
    load_gui()
