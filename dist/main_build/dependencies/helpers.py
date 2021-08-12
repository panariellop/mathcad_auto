"""
Helper Functions - misc 
"""
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
    elif input_units == "N" and target_units == "lbf":
        return value * 0.2248089
    elif input_units == "lbf" and target_units == "N":
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
    # get the file extension - how we check if the filetype is proper
    type = filename.split(".")[-1] 
    if type != filetype:
        return False
    return True



def resource_path(relative_path):
    """
    Determines the resource path for a graphic, etc
    """
    import sys 
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def walklevel(path, depth = 1):
    """It works just like os.walk, but you can pass it a level parameter
       that indicates how deep the recursion will go.
       If depth is 1, the current directory is listed.
       If depth is 0, nothing is returned.
       If depth is -1 (or less than 0), the full depth is walked.
    """
    # If depth is negative, just walk
    # Not using yield from for python2 compat
    # and copy dirs to keep consistant behavior for depth = -1 and depth = inf
    if depth < 0:
        for root, dirs, files in os.walk(path):
            yield root, dirs[:], files
        return
    elif depth == 0:
        return

    # path.count(os.path.sep) is safe because
    # - On Windows "\\" is never allowed in the name of a file or directory
    # - On UNIX "/" is never allowed in the name of a file or directory
    # - On MacOS a literal "/" is quitely translated to a ":" so it is still
    #   safe to count "/".
    base_depth = path.rstrip(os.path.sep).count(os.path.sep)
    for root, dirs, files in os.walk(path):
        yield root, dirs[:], files
        cur_depth = root.count(os.path.sep)
        if base_depth + depth <= cur_depth:
            del dirs[:]

def format_comment(comment:str)->str:
    """
    Formats the comments properly since comments come as garbled text from the excel API 
    """
    out = comment.split("Comment:")
    out = out[-1]
    #check if there are valid characters 
    is_valid = False 
    for char in out:
        ascii = ord(char)
        if (ascii >=33 and ascii <=126): 
            #from  ascii characters ! to ~ https://www.asciitable.com/
            is_valid = True 
    if is_valid: return out 
    else: return "" 

def get_input_from_info(event:str)->str:
    """
    when clicking the info button, we can pull the corresponding input 
    mounting_location_info -> mounting_location
    """
    out = event.split("_")[0:-1]
    out = "_".join(out)
    return out

if __name__ == "__main__":
    pass 
