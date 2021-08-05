#############################################
# Updater to the Mathcad Anchorage Software #
#############################################
# By: Piero Panariello
# Date: August 2021

import PySimpleGUI as sg
from main_build.dependencies.images import images 

def main(dev = False):
    layout = [
        [sg.Text("Updates") ], 
    ]
    sg.theme = ('reddit')
    sg.set_options(icon=images.ma_logo_png)


    window = sg.Window("Updater", layoyt, return_keyboard_events = True)
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break #ends gui
        else:
            #MAIN LOGIC
            

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-dev": main(dev = True )
    else: main()
