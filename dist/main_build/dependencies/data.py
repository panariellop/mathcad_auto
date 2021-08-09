"""
All the important data structures in the application 

"""
try:
    from main_build.dependencies import helpers
    from main_build.dependencies import verbose
except:
    import helpers
    import verbose 
class Equipment():
    """
    Equipment class that holds the information of all the equipment
    """

    def __init__(self):
        self.items = list()
        self.cur_index = 0
        self.fields = list()
        self.names = list()
        self.inputs = list()
        self.mounting_locations = list()
        self.outputs = list()

    def append(self, to_append: dict):
        """
        Add an eqipment to this class by appending self.items, self.names under
        specific circumstances, and self.inputs if

        argument is a dictionary
        """
        self.items.append(to_append)
        blank_outputs = Outputs()
        self.outputs.append(blank_outputs) 
        for key, field in to_append.items():  # key value pair
            if key not in self.fields:  # append fields - this is the first row in the excel document
                self.fields.append(key)
            if key == 'eqpt_name' or key == "Equipment Name":  # append names of equiptment (always the first column in the template file)
                self.names.append(field[0])
            if key == "mounting_location" and field[0] not in self.mounting_locations:
                self.mounting_locations.append(field[0])
            if key.split("_")[-1] == "input" and key not in self.inputs:
                self.inputs.append(key)
        return

    def next_index(self):  # don't want to throw out of bounds error !
        """
        Incriment cur_index to the next index
        """
        self.cur_index = (self.cur_index + 1) % len(self.items)

    def prev_index(self):
        """
        Decriment cur_index to the previous index
        """
        if self.cur_index == 0:
            self.cur_index = len(self.items) - 1
        else:
            self.cur_index -= 1

    def display_choose_eqpt(self) -> list:
        """
        Converts the names of the equipment to a list and provides the number to the left
        ex: ['1. Anesthesia Machine', ...]
        """
        output = list()
        for idx, name in enumerate(self.names):
            output.append(str(idx + 1) + ". " + name)
        return output


class Outputs():
    """
    Class that stores the information that gets presented to the user when they
    click "preview calculation outputs"
    """
    def __init__(self):
        self.items = list()
        """
        ['f_p_max_output', [408.81554560308007, 'kg', 0]]
        ['f_p_min_output', [76.65291480057748, 'kg', 0]]
        ['f_p_tot_output', [76.65291480057748, 'kg', 0]]
        """

    def append(self, to_append):
        """
        convert to_append to list and append self.items
        """
        name = to_append[0]
        values = list(to_append[1])  # need to convert from tuple to array bc tuple is immutable
        self.items.append([name, values])

    def clear(self):
        """
        Clear self.items
        """
        self.items = []

    def display_asd(self) -> list:
        """
        Presents self.items in a more displayable format so the GUI has an easier time
        """
        to_display = list()
        for i in self.items:
            if verbose.is_asd_output(i[0]):
                to_display.append(verbose.outputs(i[0]) + " = " + str(round(i[1][0], 2)) + " " + str(i[1][1]))  # name = value units
        return to_display
    def display_lrfd(self)->list:
        """
        Presents self.items in a more displayable format so the GUI has an easier time
        """
        to_display = list()
        for i in self.items:
            if verbose.is_lrfd_output(i[0]):
                to_display.append(verbose.outputs(i[0]) + " = " + str(round(i[1][0], 2)) + " " + str(i[1][1]))  # name = value units
        return to_display
    def display_misc(self)->list: 
        """
        Presents self.items in a more displayable format so the GUI has an easier time
        """
        to_display = list()
        for i in self.items:
            if not verbose.is_asd_output(i[0]) and not verbose.is_lrfd_output(i[0]):
                to_display.append(verbose.outputs(i[0]) + " = " + str(round(i[1][0], 2)) + " " + str(i[1][1]))  # name = value units
        return to_display

    def convert_units(self, in_units, tg_units):
        """
        Convert units: <input> is 'imperial' or 'metric' ; <target> is 'imperial' or 'metric'
        Uses the global function convert_units
        """
        for i in self.items:
            if in_units == "imperial" and tg_units == 'metric':  # convert from imperial to metric
                if i[1][1] == "in":
                    i[1][1] = "m"
                    i[1][0] = helpers.convert_units(i[1][0], "in", "m")
                if i[1][1] == "ft":
                    i[1][1] = "m"
                    i[1][0] = helpers.convert_units(i[1][0], "ft", "m")
                if i[1][1] == "lb":
                    i[1][1] = "kg"
                    i[1][0] = helpers.convert_units(i[1][0], "lb", "kg")
                if i[1][1] == "lbf":
                    i[1][1] = "N"
                    i[1][0] = helpers.convert_units(i[1][0], "lb", "N")
            else:
                if i[1][1] == "m":
                    i[1][1] = "ft"
                    i[1][0] = helpers.convert_units(i[1][0], "m", "ft")
                if i[1][1] == "kg":
                    i[1][1] = "lb"
                    i[1][0] = helpers.convert_units(i[1][0], "kg", "lb")
                if i[1][1] == "N":
                    i[1][1] = "lbf"
                    i[1][0] = helpers.convert_units(i[1][0], "N", "lbf")

if __name__ == "__main__":
    pass 
