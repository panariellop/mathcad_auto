import os, sys
from MathcadPy import Mathcad, Worksheet
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

def open_worksheet(mathcad_app, filename:str)->Worksheet:
    filepath = os.getcwd() + '\\' + filename
    return mathcad_app.open(filepath)

def set_inputs(worksheet:Worksheet):


def main():
    mathcad_app = Mathcad(visible = True)
    print(f"Mathcad version: {mathcad_app.version}")
    cur_worksheet = open_worksheet(mathcad_app, 'test.mcdx')
    cur_worksheet.set_real_input('a', 16)

if __name__ == "__main__":
    load_gui()