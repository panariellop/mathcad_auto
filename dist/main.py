#########################################
# Mathcad Anchorage Automation Software #
#########################################
# By: Piero Panariello
# Created: July 2021
from main_build.dependencies.filestream import get_eqpt_from_xl
import os, sys

sys.path.append(os.getcwd() + "/main_build/MathcadPy")  # allows inport of mathcad module
# from MathcadPy import Mathcad, Worksheet
# imports the images as binaries
#from images import *
from main_build.images import images
from main_build.dependencies import helpers
from main_build.dependencies import reports
from main_build.dependencies import filestream
from main_build.dependencies.data import *
from main_build.dependencies.gui import *
from main_build.dependencies.validation import InputValidation

import PySimpleGUI as sg
# needed to open excel files
# needed for parrallel processing
import threading
# so user can copy to clipboard
import pyperclip

def load_inputs(equipment: Equipment):
    """
    Takes in the equipment being viewed by the user and returns all the input
    fields with sg parts
    """
    input_fields = list()
    num_fields = 0
    for field, value in equipment.items[equipment.cur_index].items():  # each eqpt is a dictionary, field is key
        to_append = []
        name = field.split("(")[0]
        name = name.replace(" ", "")
        from main_build.dependencies import verbose #verbose names (more legible names) 
        name  = verbose.inputs(name) 
        if num_fields % 2 == 0:
            if field == 'mounting_location': #create dropdown for mounting location 
                    to_append.append(sg.Text(str(name), size = (20,1)))
                    to_append.append(sg.Combo(equipment.mounting_locations, default_value = equipment.items[equipment.cur_index]['mounting_location'][0], key = str(field), size = (28,1)))
            else:
                    to_append.append(sg.Text(str(name), size=(20, 1)))
                    to_append.append(sg.InputText(value[0], background_color = "white", size=(30, 1), key=str(field), enable_events=True))
        else:
            if field == 'mounting_location':
                    to_append.append(sg.Text(str(name), size = (20,1)))
                    to_append.append(sg.Combo(equipment.mounting_locations, default_value = equipment.items[equipment.cur_index]['mounting_location'][0], key = str(field), size = (28,1)))
            else:
                to_append.append(sg.Text(str(name), size=(20, 1), background_color = "light gray"))
                to_append.append(sg.InputText(value[0], background_color = "light gray", size=(30, 1), key=str(field), enable_events=True))
        # units 
        to_append.append(sg.Text(value[1], size = (4, 1)))
        if value[2] != "":
            #info button 
            to_append.append(sg.Button("i", key = (field+"_info"), enable_events = True))
        input_fields.append(to_append)
        num_fields += 1 
    return input_fields


def update_inputs(equipment: Equipment, values, window):
    """
    Updates the window with the inputs values to reflect the object selected
    Also updates the excel spreadsheet with the values you changed 
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
    image = files.images[mounting_location]
    return image


def load_gui(pick_files = False):
    """
    Main GUI - controlls graphics and logic
    """
    files = SelectTemplates()
    input_validation = InputValidation()
    if pick_files: #skip the choose file menu
        files.dev_get_xl_and_templates()
    else: #
        files.display_and_update()
    files.get_images_from_xl(num_images=4)
    equipment = filestream.get_eqpt_from_xl(files.excel)  # initial loading of eqpt data
    outputs = Outputs()  # preview output object
    sg.theme('Reddit')
    sg.set_options(icon=images.ma_logo_png)


    
    layout = [
        [sg.Column([[sg.Image(data = images.tt_logo)]], justification='l',  k='-C-')],

        [
            # list of equiptment
            sg.Column([
                [sg.Frame("Choose Equipment", [
                    [sg.Listbox(values=equipment.display_choose_eqpt(),
                                size=(30, 33),
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
                ])],
            ]),
            sg.Column([
                [sg.Frame("Seismic Design Parameters and Geometry",
                          load_inputs(equipment)
                          )],
            ]),
            sg.Column([
                [
                    sg.Frame("Preview Images Per Mounting Location", [[sg.Image(key = "preview_image", data = update_preview_image(equipment, files))]])
                ]
            ]), 
            sg.Column([
                [sg.Frame("Outputs",
                          [
                              [sg.Radio("Imperial Units", "RADIO1", key="convert_to_imperial", enable_events=True,
                                        tooltip="Switch outputs to imperial units."),
                               sg.Radio("Metric Units", "RADIO1", default=True, key="convert_to_metric",
                                        enable_events=True, tooltip="Switch outputs to metric units.")],
                                [sg.Text("ASD Outputs")], 
                              [sg.Listbox(values=[],
                                          size=(20, 8),
                                          key='asd_outputs',
                                          select_mode="LISTBOX_SELECT_MODE_BROWSE",
                                          right_click_menu=['&Right', ["Copy"]],
                                          enable_events=True)],
                                [sg.Text("LRFD Outputs")], 
                              [sg.Listbox(values=[],
                                        size=(20, 8),
                                        key='lrfd_outputs',
                                        select_mode="LISTBOX_SELECT_MODE_BROWSE",
                                        right_click_menu=['&Right', ["Copy"]],
                                        enable_events=True)],
                                [sg.Text("Misc. Outputs")], 
                              [sg.Listbox(values=[],
                                        size=(20, 8),
                                        key='misc_outputs',
                                        select_mode="LISTBOX_SELECT_MODE_BROWSE",
                                        right_click_menu=['&Right', ["Copy"]],
                                        enable_events=True)],
                              [sg.Button("Preview Calculation Outputs", key="calculate",
                                         tooltip="This will calculate the designated outputs for the current inputs and display them in the output field.")],
                               [
                                sg.Button("Generate Report", key="generate_report", size=(17, 1),
                                        tooltip="This will save a Mathcad report for the equipment being viewed. \nThe template file corresponding to the mounting location will be used."),
                                ],

                                [
                                sg.Button("Generate Report For All", key="generate_report_for_all",
                                        tooltip="This will generate a Mathad report for all the equipment listed.\nTemplate files corresponding to each equipment's mounting location will be used.")
                                ],
                                ],

                          element_justification = 'c'), ],

            ], justification = 'c')

        ],

     

    ]

        # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Select Input Files', '---', '&Save Inputs To Excel']],
                ['&Edit', ['&Undo', '---', '&Revert Inputs']],
            ['&Help', '&Help'],]

    layout += [[sg.Menu(menu_def)]]

    window = sg.Window('Anchorage Mathcad Automation', layout, return_keyboard_events=True)

    """==============================================="""
    """Logic loop"""
    """==============================================="""
    user_actions = UserActions()
    while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break  # ends gui
        else:
            """
            Change Input Files
            """
            if event == "Select Input Files" or event == "i:73":
                files.display_and_update()

            """
            Undo changes 
            """
            if event == "Undo":
                #need to pop the latest action from the stack 
                user_actions.clear()
                equipment = get_eqpt_from_xl(files.excel) 
                continue 
            if event == "Revert Inputs":
                while True:
                    event, value = user_actions.pop()
                    if event is not None:
                        equipment.items[equipment.cur_index][event][0] = value
                        window[event].update(value)
                    else: #reached the end of the stack 
                        break 
                continue 
            """
            If user wants to copy output
            """
            if event == "asd_outputs" or event == "lrfd_outputs" or event == "misc_outputs":
                try:
                    to_copy = window[event].get()[0]
                    pyperclip.copy(str(to_copy)) #uses pyperclip to copy to user's clipboard
                except:
                    pass
            """
            Get info for inputs 
            """
            if helpers.get_input_from_info(event) in equipment.fields:
                field = helpers.get_input_from_info(event)
                print(equipment.items[equipment.cur_index]['eqpt_name'][0])
                popup = Popup(equipment.items[equipment.cur_index]['eqpt_name'][0], equipment.items[equipment.cur_index][field][2])
                popup.alert()
                continue

            """
            Update the Equipment object when the user edits an input field
            """
            if event in equipment.fields:
                # change the cur eqpt field being edited
                user_actions.push((event, equipment.items[equipment.cur_index][event][0]))
                equipment.items[equipment.cur_index][event][0] = values[event]
                continue 
                
            """
            Save equipment back to excel 
            """
            if event == "Save Inputs To Excel" or event == 's:83': #Ctrl-s
                # update the excel file
                filestream.save_eqpt_to_xl(equipment, files.excel)

            """
            Move to the next or previous eqpt
            """
            if (event == "next" or event == "previous") and input_validation.validate(equipment):
                if event == "next":
                    equipment.next_index()
                if event == "previous":
                    equipment.prev_index()
                if files.excel != "" and helpers.check_file_type(files.excel, 'xlsx'):
                    values, window = update_inputs(equipment, values, window) #update inputs
                    # Update the outputs in the GUI
                    window['asd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_asd())
                    window['lrfd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_lrfd())
                    window['misc_outputs'].update(values=equipment.outputs[equipment.cur_index].display_misc())
                 # display the current one being selected
                window['equipment_list'].set_focus(equipment.cur_index) 
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                window['preview_image'].update(data = update_preview_image(equipment, files)) 

            """
            Display the eqpt being selected by the listbox (left most column)
            """
            if event == "equipment_list" and input_validation.validate(equipment):
                # get the current index
                equipment.cur_index = window['equipment_list'].get_indexes()[0]
                # update viewport
                values, window = update_inputs(equipment, values, window)
                #Update the output in the GUI 
                window['asd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_asd())
                window['lrfd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_lrfd())
                window['misc_outputs'].update(values=equipment.outputs[equipment.cur_index].display_misc())
                window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                window['preview_image'].update(data = update_preview_image(equipment, files)) 


            """
            Go to a specific eqpt number
            """
            if event == "goto_eqpt" and input_validation.validate(equipment):
                if values['goto_eqpt'] != "" and int(values['goto_eqpt']) <= len(equipment.items):
                    equipment.cur_index = int(values['goto_eqpt']) - 1
                    # update the inputs in the window
                    values, window = update_inputs(equipment, values, window) 
                    # display the eqpt being selected
                    window['equipment_list'].set_focus(equipment.cur_index)  
                    # update the outputs in the GUI
                    window['asd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_asd())
                    window['lrfd_outputs'].update(values=equipment.outputs[equipment.cur_index].display_lrfd())
                    window['misc_outputs'].update(values=equipment.outputs[equipment.cur_index].display_misc())
                    window['cur_eqpt'].update(f'Equipment {equipment.cur_index + 1}/{len(equipment.items)} loaded')
                    window['preview_image'].update(data = update_preview_image(equipment, files)) 


            """
            Generate report for one eqpt
            """
            if event == "generate_report" and input_validation.validate(equipment):
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
            if event == "generate_report_for_all" and input_validation.validate(equipment):
                # check if the files exist and are the correct file type
                if files.excel == "" or helpers.check_file_type(files.excel, "xlsx") != True:
                    popup = Popup("Error", "Please select an input excel file.")
                    popup.alert()
                else:
                    errors = []
                    for eqpt in equipment.items:
                        status = reports.pre_generate_report(equipment=equipment, files=files, cur_directory=os.getcwd(), generating_multiple_reports=True)
                        if not status:
                            errors.append(f'There was an issue processing {eqpt["eqpt_name"]}')
                    for k, v in files.templates.items():
                        for i in range(len(equipment.items)):
                            try:
                                os.remove(v.split(".")[0]+str(i)+".mcdx")
                            except: continue
                    if len(errors)>0:
                        popup = Popup("Error", "\n".join(errors))
                        popup.alert()
                    else:
                        popup = Popup("Success", "Successfuly saved reports.")
                        popup.alert()
                continue 
                

            """
            Generate Report for all eqpt
            """
            if event == "generate_report_for_all" and input_validation.validate(equipment):
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
            if event == "calculate" and input_validation.validate(equipment):
                #check if the excel file exists
                if files.excel == "":
                    alert = Popup("Error", "Please select an input excel file from the input files window.")
                    alert.alert()
                else:
                    outputs = reports.mathcad_calculate(equipment, files.templates[equipment.items[equipment.cur_index]['mounting_location'][0]])
                    #add all the output we got from mathcad_calculate to the outputs class
                    cur_outputs = equipment.outputs[equipment.cur_index]
                    cur_outputs.clear() #clear to prep for next inputs
                    from main_build.dependencies import verbose 
                    for key, val in outputs.items():
                        cur_outputs.append([key, val]) 
                    window['asd_outputs'].update(values=cur_outputs.display_asd())
                    window['lrfd_outputs'].update(values=cur_outputs.display_lrfd())
                    window['misc_outputs'].update(values=cur_outputs.display_misc())
                    alert = Popup("Calcuation Complete", "Output fields have been updated.")
                    alert.alert()

            """
            Convert Units
            """
            if event == "convert_to_imperial":
                cur_outputs = equipment.outputs[equipment.cur_index] 
                cur_outputs.convert_units('metric', 'imperial')
                window['asd_outputs'].update(values=cur_outputs.display_asd())
                window['lrfd_outputs'].update(values=cur_outputs.display_lrfd())
                window['misc_outputs'].update(values=cur_outputs.display_misc())
            if event == "convert_to_metric":
                cur_outputs = equipment.outputs[equipment.cur_index] 
                cur_outputs.convert_units('imperial', 'metric')
                window['asd_outputs'].update(values=cur_outputs.display_asd())
                window['lrfd_outputs'].update(values=cur_outputs.display_lrfd())
                window['misc_outputs'].update(values=cur_outputs.display_misc())
            """Get help"""
            if event == "Help":
                popup = Popup("Get Help", "---File Manipulation---\nFile->Select or Ctrl-i to select input files \nFile->Save or Ctrl-s to save inputs back to the excel file\n\n---Inquiries---\nPlease direct all inquires to Parth Korde <PKorde@ThorntonTomasetti.com>, Richard Kuo <RKuo@ThorntonTomasetti.com>, or Theresa Curtis <TCurtis@ThorntonTomasetti.com>. Please consult the documentation first:")
                popup.link("Documentation", "https://github.com/panariellop/mathcad_auto/blob/master/user_guide.pdf") 

    window.close()
    del window
    return










if __name__ == "__main__":
    #TODO ensure pick_files is set to false when packaging application
    #pick_files is another way of saying developer environment  
    #pick_files hides the menu to choose input files when True 
    load_gui(pick_files=True)
