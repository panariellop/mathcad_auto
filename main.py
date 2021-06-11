import os, sys
sys.path.insert(1, os.getcwd() + "\\build\\MathCadPy")
from mathcadpy import Mathcad, Worksheet #loading custom 
# from MathcadPy import Mathcad, Worksheet
import PySimpleGUI as sg
from pathlib import Path, PurePath

def load_gui():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Check Mathcad Version"), sg.Button("Check", key = "-CHECKVER-")],
        [sg.Text('Value1'), sg.InputText(key = "-IN1-"), sg.Text("kg")],
        [sg.Text('Value2'), sg.InputText(key = "-IN2-")],
        [sg.Text('Value3'), sg.InputText(key = "-IN3-")],
        [sg.Text('Value4'), sg.InputText(key = "-IN4-")],
        [sg.Text("File Name"), sg.InputText(key = '-SAVEFILENAME-')],
        [sg.Text(key = "-STATUS-")],
        [sg.Button('Generate file'), sg.Button('Clear Inputs', key = '-CLEAR-')],
    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)
    while True: #gui loop 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
    window.close()

def open_worksheet(mathcad_app, relative_filepath:str)->Worksheet:
    filepath = os.getcwd() + '\\' + relative_filepath
    return mathcad_app.open(filepath)

def save_worksheet_as(worksheet, filename:str):
    filepath = os.getcwd() + "\\" + filename
    try:
        worksheet.save_as(filepath)
        return True 
    except:
        return False


def main(debug = False):
    mathcad_app = Mathcad(visible = debug)
    print(f"Mathcad version: {mathcad_app.version}")
    cur_worksheet = open_worksheet(mathcad_app, 'test.mcdx')
    cur_worksheet.set_real_input('a', 16)
    save_worksheet_as(cur_worksheet, "test5.mcdx")
    cur_worksheet.close()

if __name__ == "__main__":
    main(debug = True)