import os, sys
sys.path.insert(1, os.getcwd() + "\\build\\MathCadPy")
from mathcadpy import Mathcad, Worksheet #loading custom 
# from MathcadPy import Mathcad, Worksheet
import PySimpleGUI as sg
from pathlib import Path, PurePath
class Popup():
    def __init__(self, title, message):
        self.title = title
        self.message = message
    def confirm(self)->bool:
        popup = sg.Window(self.title, [
                        [sg.Text("")],
                        [sg.Text(self.message), sg.Button("YES", key = "YES"), sg.Button("NO", key = "NO")],
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
    layout = [
        [sg.Text("Check Mathcad Version"), sg.Button("Check", key = "-CHECKVER-"), sg.Text(key = "-VER-", size = (20,1))],
        [sg.Text("")],
        [sg.Text("Load template file..."), sg.Input(size = (25, 1)), sg.FileBrowse(key = "-TEMPLATE_FILE-")],
        [sg.Text("")],
        [sg.Text('Value1'), sg.InputText(key = "-IN1-"), sg.Text("kg")],
        [sg.Text('Value2'), sg.InputText(key = "-IN2-")],
        [sg.Text('Value3'), sg.InputText(key = "-IN3-")],
        [sg.Text('Value4'), sg.InputText(key = "-IN4-")],
        [sg.Text('', size = (2,1))],
        [sg.Text("File Name"), sg.InputText(key = '-SAVEFILENAME-', size = (15,1)), sg.Text(".mcdx")],
        [sg.Text(key = "-STATUS-", size = (20,3))],
        [sg.Button('Generate file', key = "-GEN-"), sg.Button('Clear Inputs', key = '-CLEAR-')],
    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)
    while True: #gui loop 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
        else:
            if event == "-CHECKVER-":
                mathcad_app = Mathcad(visible = False)
                window['-VER-'].update("Mathcad Version: " + str(mathcad_app.version))
            elif event == "-CLEAR-":
                #creates confirming popup and then clears values
                popup = Popup("Confirm clear", "Are you sure you want to clear all inputs?")
                if popup.confirm() == True:
                    inputs = ["-IN1-", "-IN2-","-IN3-","-IN4-"]
                    for key in inputs:
                        window[key].update("")
                        values[key] = "" 
            elif event == "-GEN-": #perform calculations  
                status = generate_file(values, debug = False)
                if status:
                    status = "File saved."
                else:
                    status = "Error saving file."
                values['-STATUS-'] = status 
                window['-STATUS-'].update(status)




    window.close()
    return 

             
def save_worksheet_as(worksheet, filename:str)->bool:
    filepath = os.getcwd() + "\\" + filename
    try:
        worksheet.save_as(filepath)
        return True 
    except:
        return False

def generate_file(values, debug = False)->bool:
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
