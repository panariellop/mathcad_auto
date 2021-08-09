class InputValidation():
    """
    Call validate to check all inputs 
    Example equipment item 
    [{'eqpt_name': ['Anesthesia Machine ', ''], 'eqpt_number': [1234, ''], 'mounting_location': ['Wall, Floor', ''], 'project_number': [1111, ''], 'tags': ['Medical, ICU, something', ''], 'w_p_input': [335, 'lb'], 's_ds_input': [1.121, ''], 'a_p_input': [1, ''], 'r_p_input': [2.5, ''], 'i_p_input': [1.5, ''], 'z_input': [0, ''], 'h_input': [75,5, ''], 'factor_input': [0.666666, '']}
    """
    def __init__(self):
        self.errors = []
    def validate(self, equipment, debug = False):
        """
        Validates all the equipment 
        """
        self.errors = []
        for e in equipment.items:
            self.mounting_location(e, equipment)
            self.input_values(e)
        #Check if any errors have occured 
        if len(self.errors) > 0:
            if debug == False:
                try:
                    from main_build.dependencies.gui import Popup
                except:
                    from gui import Popup
                popup = Popup("Errors", "; ".join(self.errors))
                popup.alert()
            else:
                print(self.errors) 
            return False
        else: return True 
            
    def mounting_location(self,cur_eqpt, eqpt):
        """
        Mounting location needs to be mentioned in the excel file 
        """
        mounting_location = cur_eqpt['mounting_location']
        if mounting_location[0] in eqpt.mounting_locations:
            #Check if the mounting location is in the templates
            pass
        else:
            self.errors.append(f"{cur_eqpt['eqpt_name'][0]}: mounting location must be one of the mounting locations mentioned in the input excel file. {mounting_location[0]} is not mentioned.")
            
    def input_values(self, cur_eqpt):
        """
        Checks if input values are within the correct ranges
        """
        eqpt_name = cur_eqpt['eqpt_name']
        pos_inputs = ['w_p_input',
                      's_ds_input',
                      'a_p_input',
                      'r_p_input',
                      'omega_input',
                      'z_input',
                      'h_input',
                      'capital_a_input',
                      'capital_b_input',
                      ]
        plus_minus_inputs = ['b_input',
                             'a_input',] 

        for i in pos_inputs:
            try:
                if int(cur_eqpt[i][0]) < 0:
                    self.errors.append(f"{eqpt_name[0]}: {i} should be greater than 0")
            except:
                pass
        for i in plus_minus_inputs:
            try:
                if int(cur_eqpt[i][0]) == 0:
                    self.errors.append(f"{eqpt_name[0]}: {i} should be greater than or less than 0")
            except:pass
        

if __name__ == "__main__":
    pass 
