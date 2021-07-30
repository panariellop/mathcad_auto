from openpyxl import Workbook as xlwkbk
from openpyxl import load_workbook
from openpyxl_image_loader import SheetImageLoader
from main_build.images import images
from main_build.dependencies import helpers
from main_build.dependencies import filestream
from main_build.dependencies.data import *

import PySimpleGUI as sg

class SelectTemplates():
    """
    This is the select templates window that users can use to edit or add
    templates to the program.
    """

    def __init__(self):
        self.database = ""
        self.save_to_database = True
        self.excel = ""
        self.template_layout = []
        self.templates = {}
        self.wall_template = ""
        self.floor_template = ""
        self.wallfloor_template = ""
        self.ceiling_template = ""
        self.images = dict()
        self.can_continue = False

    def choose_templates(self):
        sg.theme("Reddit")
        window = sg.Window("Choose Template Files", [
            self.template_layout,
            [sg.Button("Continue", key = "continue", button_color = "green", enable_events = True)]
        ], icon = images.ma_logo_png)
        while True: #logic loop
            event, values = window.read()
            if event == 'OK' or event == sg.WIN_CLOSED:
                window.close()
                return False
            if event == "continue":
                #set each template to the corresponding GUI item
                errors = []
                for k, v in self.templates.items():
                    if helpers.check_file_type(values[k+"_name"], "mcdx"):
                        self.templates[k] = values[k+"_name"]
                    else:
                        errors.append(k+" mounting template must be a .mcdx file.")
                #error management
                if len(errors) < 1:
                    window.close()
                    return self.templates
                else:
                    popup = Popup("Error", " ".join(errors))
                    popup.alert()


    def display_and_update(self):
        """
        Displays the window and will update the object variables when the user hits continue
        """
        sg.theme("Reddit")
        window = sg.Window("Mathcad Automation", [
            [sg.Frame("Choose Excel File*", [[sg.FileBrowse(key="excel_file", enable_events=True),
                                              sg.InputText(self.excel, key="excel_name", size=(30, 1),
                                                           background_color='white', enable_events=True),],

                                              [sg.Button("Choose Templates", key = "choose_templates", enable_events = True)],
                                            ])],
            [sg.Frame("Choose Database File", [[sg.FileBrowse(key="database_file", enable_events=True),
                                                sg.InputText(self.database, key="database_name", size=(30, 1),
                                                             background_color='white', enable_events=True)], ])],
            [sg.Checkbox("Save to database?", key="save_to_database", default=self.save_to_database,
                         tooltip="If selected, details about the generated report will be saved to a database.")],

            [sg.Button("Continue", key="continue", button_color="green")],

        ], icon=images.ma_logo_png)
        """Listen for events"""
        while True: #logic loop
            event, values = window.read()
            if event == 'OK' or event == sg.WIN_CLOSED:
                window.close()
                return False
            else:
                if event == "choose_templates":
                    """
                    load the excel file and search for different mounting locations
                    """
                    if helpers.check_file_type(values['excel_name'], 'xlsx'):
                        #get the mounting locations
                        equipment = filestream.get_eqpt_from_xl(values['excel_name'])
                        if len(equipment.items) > 0:
                            self.excel = values['excel_name']
                            self.template_layout = []
                            for idx, item in enumerate(equipment.mounting_locations):
                                if item not in self.templates:
                                    self.templates[item] = ""
                                #create the layout for the choose templates window
                                self.template_layout += [
                                    [sg.Text("Choose " + item + " mounting template:")],
                                    [sg.FileBrowse(key= item, enable_events=True),
                                      sg.InputText(self.templates[item], key=item + "_name",
                                      size=(60, 1), background_color='white', enable_events=True)],
                                ]
                            if self.choose_templates():
                                self.can_continue = True


                if event == "continue":  # user has input all information
                    # list of all the user errors when they input information
                    errors = list()
                    # validate the filepaths
                    self.save_to_database = values['save_to_database']
                    #check if the database is a .csv file - if not, append error list
                    if helpers.check_file_type(values['database_name'], 'csv') or values['database_name'] == "":
                        self.database = values['database_name']
                    else:
                        errors.append("Database file must be a .csv file.")
                    #check if excel file is .xlsx
                    if helpers.check_file_type(values['excel_name'], 'xlsx'):
                        self.excel = values['excel_name']
                    else:
                        errors.append("Excel file must be a .xlsx file.")
                    # Error handling
                    if len(errors) == 0 and self.can_continue: #no errors
                        window.close()
                        return True
                    elif self.can_continue == False:
                        alert = Popup("Error", "You must choose template files.")
                        alert.alert()
                        continue
                    else: #show errors in a popup window
                        alert = Popup("Errors", "\n".join(errors))
                        alert.alert()
                        continue

    def get_images_from_xl(self, num_images: int):
        """
        Gets all the preview images from the excel file and saves a dictionary of
        mounting locations and binary images in self.images
        <num_images:int> Corresponds to the number of mounting locations,
        indicated in the preview_images portion of the input excel document
        """
        wb = load_workbook(self.excel)
        sheet = wb['preview_images']

        image_loader = SheetImageLoader(sheet)
        for i in range(num_images):
            # hard coded
            mounting_locations = ['wall', 'floor', 'wall,floor', 'ceiling']
            try:  # load all the images in cells B2-5
                image = image_loader.get('B' + str(i + 2))
                buf = io.BytesIO()
                image.save(buf, format="PNG")  # save as a bytes string so pysimplegui can use it
                self.images[mounting_locations[i]] = buf.getvalue()
            except Exception as e:
                print(e)


class Popup():
    """
    Simple class to create a popup window. Used to create a popup to input filenames,
    display errors, etc.
    """
    def __init__(self, title, message=""):
        self.title = title
        self.message = message

    def confirm(self) -> bool:
        """
        Confirmation window - if you want to confirm with the user yes/no
        """
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message), ],
            [sg.Text("")],
            [sg.Button("YES", key="YES", button_color='green'), sg.Button("NO", key="NO", button_color='red')],
        ],
                          icon=images.ma_logo_png, )
        while True:
            event, values = popup.read()
            if event == "OK" or event == "NO" or event == sg.WIN_CLOSED:
                popup.close()
                return False
            if event == "YES":
                popup.close()
                return True

    def alert(self):
        """
        Alert window - alert the user with a message
        """
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message)],
            [sg.Button("OK", key='OK', button_color='green')],
        ],
                          icon=images.ma_logo_png, )
        while True:
            event, values = popup.read()
            if event == "OK" or event == sg.WIN_CLOSED:
                popup.close()
                break
            else:
                pass

    def take_input(self, trailing_text: str) -> str:
        """
        Input window - if you want the user to input some information
        """
        popup = sg.Window(self.title, [
            [sg.Text("")],
            [sg.Text(self.message), sg.InputText(key="input", size=(15, 1)), sg.Text(trailing_text)],
            [sg.Button("OK", key='OK', button_color='green')],
        ],
                          icon=images.ma_logo_png, )
        while True:
            event, values = popup.read()
            if event == "OK" or event == sg.WIN_CLOSED:
                popup.close()
                return values['input']

    def image(self, image):
        """
        Creates a popup window with title and image
        """
        popup = sg.Window(self.title, [
            [sg.Image(data=image)]
        ])
        while True: #logic loop
            """
            Window will stay active until the user exits the window or they click the OK buttion
            """
            event, values = popup.read()
            if event == "OK" or event == sg.WIN_CLOSED:
                popup.close()
                break


if __name__ == "__main__":
    pass
