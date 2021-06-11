import os, sys
from MathcadPy import Mathcad
import PySimpleGUI as sg

def load_gui():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Hello world..")],
        [sg.Text('Value1'), sg.InputText(key = "-IN1-"), sg.Text("kg")],
        [sg.Text('Value2'), sg.InputText(key = "-IN2-")],
        [sg.Text('Value3'), sg.InputText(key = "-IN3-")],
        [sg.Text('Value4'), sg.InputText(key = "-IN4-")],
        [sg.Text(key = "-STATUS-")],
        [sg.Button('Generate file')],
    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)
    while True: #gui loop 
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui 
    window.close()

def open_worksheet(mathcad_app, filename):
    pass

def main():
    mathcad_app = Mathcad()
    print(f"Mathcad version: {mathcad_app.version}")

if __name__ == "__main__":
    main()