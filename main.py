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

        [sg.Column([
            [sg.Frame("Choose Excel File", [[sg.FileBrowse(key = "excel_file"), sg.Text(key = "-EXCEL_NAME-", size = (50,1), background_color = 'white')], ])],
        ]),
        sg.Column([
            [sg.Frame("Choose template", [[sg.FileBrowse(key = "template_file"), sg.Text(key = "-TEMPLATE_NAME-", size = (50,1), background_color = 'white')], ])],
        ]),
        ],

                  
        [sg.Text("Eqipment Name: "), sg.InputText(key = "eqpt_name", size = (30, 1), background_color = "yellow"), sg.Text("Mounting Location: "), sg.Combo(["WALL","CEILING", "FLOOR", "FLOOR+WALL"], enable_events = True, key = "mounting_location")],

        [
        sg.Text("W_p :="), sg.InputText("", size=(4,1), key = "w_p_input"), sg.Text("lbf", size = (60,1)),
        sg.Button("Calculate", key = "calculate"), 
        sg.Text("File Name"), sg.InputText(key = 'save_file_name', size = (15,1)), sg.Text(".mcdx"),
        sg.Frame("", [[
            sg.Button("Generate Report", key = "generate_report"), 
        ],
        [
            sg.Button("Previous", key="previous"), sg.Button("Next", key = "next")
        ]
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
                [sg.Text("CG_y:= 2/3 * H =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_y_ouput", background_color='yellow')], 
                [sg.Text("CG_X1:= A/2 =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_x1_ouput", background_color='yellow')], 
                [sg.Text("CG_X2:= B/2 =", size = (15, 1)), sg.InputText(size = default_input_size, key = "cg_x2_ouput", background_color='yellow')], 


            ]
            , size = (100,-1))]
            ]),


            #preview images
        sg.Column([
                [sg.Frame("Preview Images", [
                    [sg.Text("Input images")], 
                ])]
            ]),

            ],

        [sg.Column([[
            sg.Frame("DETERMINE SEISMIC FORCE", [ #first column
                [sg.Text("F_p"), 
                    sg.Image(filename = (os.getcwd() + "\\build\images\\rsz_f_p_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_output"),
                    ],
                [sg.Text("F_p_max"), 
                    sg.Image(filename = (os.getcwd() + "\\build\images\\rsz_f_p_max_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_max_output"),
                    ],
                [sg.Text("F_p_min"), 
                    sg.Image(filename = (os.getcwd() + "\\build\images\\rsz_f_p_min_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_min_output"),
                    ],
                [sg.Text("F_p"), 
                    sg.Image(filename = (os.getcwd() + "\\build\images\\rsz_f_p_tot_equation.png")), 
                    sg.Text("="), sg.InputText(size = default_input_size, background_color='yellow', key = "f_p_tot_output"),
                    ],
            
            ]
            ,size = (100, -1))
            ]]), sg.Column([ #second column
               [sg.Frame("DETERMINE SEISMIC FORCE", [
                    [sg.Text("Connection to equipment"), sg.Combo(["ASD", "LRFD"], enable_events = True, key = "connection_to_eqpt")],
                    [sg.Text("Load Combinations:")], 
                    [sg.Text("F_PV:="), sg.InputText("", key = "f_pv_connection_to_eqpt", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],
                    [sg.Text("F_PH:="), sg.InputText("", key = "f_ph_connection_to_eqpt", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],

                   ])], 

            ]), sg.Column([#third column

                [sg.Frame("DETERMINE SEISMIC FORCE", [
                    [sg.Text("Connection to base"), sg.Combo(["ASD", "LRFD"], enable_events = True, key = "connection_to_base")],
                    [sg.Text("Load Combinations:")], 
                    [sg.Text("F_PV:="), sg.InputText("", key = "f_pv_connection_to_base", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],
                    [sg.Text("F_PH:="), sg.InputText("", key = "f_ph_connection_to_base", size = default_input_size, background_color = "yellow"), sg.Text("lbf")],

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
    while True: #gui loop 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
        else:
            """
            Update the maximum tension and shear anchor points labels
            """
            if event == "connection_to_base" or event == "connection_to_eqpt":
                if values["connection_to_base"] == "ASD":
                    window['base_t_max_det_label'].update("T_max=")
                    window['base_v_max_det_label'].update("T_max=")
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
