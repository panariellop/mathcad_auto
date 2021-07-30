#########################################
# Mathcad Anchorage Automation Software #
#########################################
# By: Piero Panariello
# Created: July 2021
import os, sys

sys.path.append(os.getcwd() + "/main_build/MathcadPy")  # allows inport of mathcad module
from mathcadpy import Mathcad, Worksheet  # loading custom
# from MathcadPy import Mathcad, Worksheet
# imports the images as binaries
#from images import *
from main_build.images import images
from main_build.dependencies import helpers
from main_build.dependencies import reports
from main_build.dependencies import filestream
from main_build.dependencies.data import *
from main_build.dependencies.gui import * 

import PySimpleGUI as sg
from pathlib import Path, PurePath
# needed to open excel files
from openpyxl import Workbook as xlwkbk
from openpyxl import load_workbook
# needed for parrallel processing
from shutil import copyfile
import threading
# needed to save to leger csv
import csv
import random
import copy
from datetime import date
# so user can copy to clipboard
import pyperclip
import io
from time import sleep
# so we can grab images from the sheet
from openpyxl_image_loader import SheetImageLoader
import stat





def load_inputs(equipment: Equipment):
    """
    Takes in the equipment being viewed by the user and returns all the input
    fields with sg parts
    """
    input_fields = list()
    num_fields = 0
    for field, value in equipment.items[equipment.cur_index].items():  # each eqpt is a dictionary, field is key
        name = field.split("(")[0]
        name = name.replace(" ", "")
        if num_fields % 2 == 0:
            input_fields.append( #provides some pysimplegui text and input boxes
                [sg.Text(str(name + " = "), size=(20, 1)),
                 sg.InputText(value[0], background_color = "white", size=(30, 1), key=str(field), enable_events=True),
                 sg.Text(value[1])]
            )
        else:
            input_fields.append( #provides some pysimplegui text and input boxes
                [sg.Text(str(name + " = "), size=(20, 1), background_color = "light gray"),
                 sg.InputText(value[0], background_color = "light gray", size=(30, 1), key=str(field), enable_events=True),
                 sg.Text(value[1])]
            )
        num_fields += 1 
    return input_fields


def update_inputs(equipment: Equipment, values, window):
    """
    Updates the window and value to reflect the object selected
    """
    for field, val in equipment.items[equipment.cur_index].items():
        values[field] = val[0]
        window[field].update(val[0])

    return values, window


def update_preview_image(equipment: Equipment, files):
    """
    Takes in the equipment and files and window objects and returns the image binary
    """
    mounting_location = str(equipment.items[equipment.cur_index]['mounting_location'][0])
    mounting_location = mounting_location.lower().replace(" ", "")
    # wall,floor and floor,wall handling for the preview images:
    if mounting_location == "floor,wall": mounting_location = "wall,floor"
    image = files.images[mounting_location]
    return image


def load_gui():
    """
    Main GUI - controlls graphics and logic
    """
    files = SelectTemplates()
    files.display_and_update()
    files.get_images_from_xl(num_images=4)
    print(files.templates)
    equipment = filestream.get_eqpt_from_xl(files.excel)  # initial loading of eqpt data
    outputs = Outputs()  # preview output object

    sg.theme('Reddit')
    sg.set_options(icon=images.ma_logo_png)
    layout = [

        [
            sg.Button("Change Input Files", key="change_input_files", tooltip="Reselect the input files."),
            sg.Text(" ", size=(5, 1)),
            sg.Button("Refresh", key="refresh_input_files", tooltip="Reload the data from the excel sheet.")
        ],

        [
            # list of equiptment
            sg.Column([
                [sg.Frame("Choose Equipment", [
                    [sg.Listbox(values=equipment.display_choose_eqpt(),
                                size=(30, 20),
                                key='equipment_list',
                                select_mode="LISTBOX_SELECT_MODE_SINGLE",
                                enable_events=True,
                                )],
                    [
                        sg.Button("Previous", key="previous", size=(8, 1),
                                  tooltip="Go to the previous equipment in the list."),
                        sg.Button("Next", key="next", size=(7, 1), tooltip="Go to the next equipment in the list."),
                        sg.Text(" ", size=(5, 1)),
                        sg.Text("Go to:"),
                        sg.InputText(equipment.cur_index, key="goto_eqpt", enable_events=True, size=(3, 1),
                                     tooltip="Go to a specific equipment index."),
                    ],
                    [sg.Text("Equipment: ", key="cur_eqpt", size=(20, 1), background_color="gray")],
                    [sg.Button("View Preview Image",
                               tooltip="View the image corresponding to the mounting location. This image is defined in the excel spreadsheet in the preview_images tab",
                               key="preview_image")]
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
                              [sg.Radio("Imperial Units", "RADIO1", key="convert_to_imperial", enable_events=True,
                                        tooltip="Switch outputs to imperial units."),
                               sg.Radio("Metric Units", "RADIO1", default=True, key="convert_to_metric",
                                        enable_events=True, tooltip="Switch outputs to metric units.")],

                              [sg.Listbox(values=[],
                                          size=(30, 20),
                                          key='outputs',
                                          select_mode="LISTBOX_SELECT_MODE_BROWSE",
                                          right_click_menu=['&Right', ["Copy"]],
                                          enable_events=True)],
                              [sg.Button("Preview Calculation Outputs", key="calculate",
                                         tooltip="This will calculate the designated outputs for the current inputs and display them in the output field.")],
                          ],

                          )],

            ])

        ],

        [

            sg.Frame("", [[
                sg.Button("Generate Report", key="generate_report", size=(17, 1),
                          tooltip="This will save a Mathcad report for the equipment being viewed. \nThe template file corresponding to the mounting location will be used."),
            ],

                [
                    sg.Button("Generate Report For All", key="generate_report_for_all",
                              tooltip="This will generate a Mathad report for all the equipment listed.\nTemplate files corresponding to each equipment's mounting location will be used.")
                ],
            ])],

    ]

    window = sg.Window('Anchorage Mathcad Automation', layout)

    """Logic loop"""
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break  # ends gui
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
                confirm = Popup("Confirm",
                                "This will reload the information from the input excel document and erase any changes you have made to the inputs.")
                if confirm.confirm():
                    equipment = filestream.get_eqpt_from_xl(files.excel)
                    files.get_images_from_xl(4)
                    values, window = update_inputs(equipment, values, window)

            """
            If user wants to copy output
            """
            if event == "outputs":
                try:
                    to_copy = window['outputs'].get()[0]
                    pyperclip.copy(str(to_copy)) #uses pyperclip to copy to user's clipboard
                except:
                    pass

            """
            Update the Equipment object when the user edits an input field
            """
            if event in equipment.fields:
                # change the cur eqpt field being edited
                equipment.items[equipment.cur_index][event][0] = values[event]
            if event == "preview_image":
                popup = Popup("Preview Image")
                popup.image(update_preview_image(equipment, files))

            """
            Move to the next or previous eqpt
            """
            if event == "next" or event == "previous":
                if event == "next":
                    equipment.next_index()
                if event == "previous":
                    equipment.prev_index()
                if files.excel != "" and helpers.check_file_type(files.excel, 'xlsx'):
                    values, window = update_inputs(equipment, values, window) #update inputs
                window['outputs'].update(values=[]) # clear the outputs in the GUI
                window['equipment_list'].set_focus(equipment.cur_index)  # display the current one being selected
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')

            """
            Display the eqpt being selected by the listbox (left most column)
            """
            if event == "equipment_list":
                # get the current index
                equipment.cur_index = window['equipment_list'].get_indexes()[0]
                # update viewport
                values, window = update_inputs(equipment, values, window)
                window['outputs'].update(values=[])
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')

            """
            Go to a specific eqpt number
            """
            if event == "goto_eqpt":
                if values['goto_eqpt'] != "" and int(values['goto_eqpt']) <= len(equipment.items):
                    equipment.cur_index = int(values['goto_eqpt']) - 1
                    values, window = update_inputs(equipment, values, window)  # update the inputs in the window
                    window['equipment_list'].set_focus(equipment.cur_index)  # display the eqpt being selected
                    window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')

            """
            Generate report for one eqpt
            """
            if event == "generate_report":
                # check if the files exist and are the correct file type
                if files.excel == "" or helpers.check_file_type(files.excel, "xlsx") != True:
                    popup = Popup("Error", "Please select an input excel file.")
                    popup.alert()
                else:
                    status = reports.pre_generate_report(equipment=equipment, files=files, cur_directory=os.getcwd(), generating_multiple_reports=False)
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
                """
                Using multithreading to improve speed
                Each thread is an independant process, and keeps track of its
                local variables. Once it is finished with the proces, we must
                merge all "hanging" threads into the main thread.
                """
                threads = list()
                num_threads = 16
                cur_row = 0
                equipment.cur_index = 0  # set to beginning of list
                while cur_row < len(equipment.items):
                    for i in range(num_threads):
                        if (cur_row < len(equipment.items)):
                            print(f'Processing equipment: {cur_row + 1}/{len(equipment.items)}')
                            #create a thread who's target is pre_generate_report
                            t = threading.Thread(target=reports.pre_generate_report, args=(equipment, files, os.getcwd(), True))
                            threads.append(t) #append list so we can keep track of active threads
                            t.start() #starts thread
                            cur_row += 1
                            equipment.next_index()
                        else:
                            break
                    for i in range(len(threads)):
                        threads[i].join()  # join all threads to the main thread when finished
                print("Finished threading ...")
                # cleanup files -- need to guess the file names (performance should be fine for <1000 pieces of equipment)
                for k, v in files.templates.items():
                    for i in range(len(equipment.items)):
                        try:
                            os.remove(v.split(".")[0]+str(i)+".mcdx")
                        except: continue
                alert = Popup("File saved", "All files have been saved successfuly.")
                alert.alert()

            """
            Preview
            """
            if event == "calculate":
                #check if the excel file exists
                if files.excel == "":
                    alert = Popup("Error", "Please select an input excel file from the input files window.")
                    alert.alert()
                else:
                    to_out = reports.mathcad_calculate(equipment, files.templates[equipment.items[equipment.cur_index]['mounting_location'][0]])
                    outputs.clear()  # clear the outputs to prepare for new ones
                    #add all the output we got from mathcad_calculate to the outputs class
                    for key, val in to_out.items(): outputs.append([key, val])
                    window['outputs'].update(values=outputs.display())
                    alert = Popup("Calcuation Complete", "Output fields have been updated.")
                    alert.alert()

            """
            Convert Units
            """
            if event == "convert_to_imperial":
                outputs.convert_units('metric', 'imperial')
                window['outputs'].update(values=outputs.display())
            if event == "convert_to_metric":
                outputs.convert_units('imperial', 'metric')
                window['outputs'].update(values=outputs.display())

    window.close();
    del window
    return










if __name__ == "__main__":
    load_gui()
