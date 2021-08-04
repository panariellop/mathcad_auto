"""
Helper Functions - misc 
"""

import io
import os 
import random


def convert_units(value: int, input_units: str, target_units: str) -> int:
    """
    Takes in a value and its units and outputs the value in the target units
    Supported conversions: m <-> in ; m <-> ft ; kg <-> lb ; n <-> lbf
    """
    input_units = input_units.lower()
    target_units = target_units.lower()
    if input_units == "m" and target_units == "in":
        return value * 39.37008
    elif input_units == "in" and target_units == "m":
        return value / 39.37008
    elif input_units == "m" and target_units == "ft":
        return value * 3.28084
    elif input_units == "ft" and target_units == "m":
        return value / 3.28084
    elif input_units == "kg" and target_units == "lb":
        return value * 2.204623
    elif input_units == "lb" and target_units == "kg":
        return value / 2.204623
    elif input_units == "n" and target_units == "lbf":
        return value * 0.2248089
    elif input_units == "lbf" and target_units == "n":
        return value / 0.2248089

    else:
        return value


def gen_random_string(length: int) -> str:
    """
    Generates a string of random characters
    """
    out = ""
    for i in range(length):
        char = random.randint(65, 90)
        out += chr(char)
    return out


def check_file_type(filename, filetype):
    """
    Checks if the input file is of a certain type
    ex <filename.csv> <csv>
    """
    type = filename.split(".")[-1] #get the file extension
    if type != filetype:
        return False
    return True



def resource_path(relative_path):
    """
    Determines the resource path for a graphic, etc
    """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def format_comment(comment:str)->str:
    """
    Formats the comments properly since tehy come as garbled text
    """
    out = comment.split("Comment:")
    out = out[-1]
    out = out.strip("\n")
    return out 

def get_input_from_info(event:str)->str:
    """
    mounting_location_info -> mounting_location
    """
    out = event.split("_")[0:-1]
    out = "_".join(out)
    return out 
if __name__ == "__main__":
    pass