class InputValidation():
    """
    Call validate to check all inputs 
    Validate the following inputs:
    1) Mounting Location 
    2) 
    """
    def __init__(self, equipment):
        self.equipment = equipment
        self.errors = []
    def validate(self):
        """
        Validates all the equipment 
        """
        for e in self.equipment.items:
            self.mounting_location(e, self.equipment)
            self.input_values(e)
        #Check if any errors have occured 
        if len(self.errors) == 0:
            return True
        else: return False 
            
    def mounting_location(self,cur_eqpt, eqpt):
        """
        Can have the following 
        """
        mounting_location = cur_eqpt['mounting_location']
        if mounting_location[0] in eqpt.mounting_locations:
            #Check if the mounting location is in the templates
            pass
        else:
            self.errors.append(f"{cur_eqpt['eqpt_name']}: mounting location must be one of the mounting locations mentioned in the input excel file. {mounting_location} is not mentioned.")
            
    def input_values(self, cur_eqpt):
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
            if int(cur_eqpt[i]) < 0:
                self.errors.append(f"{eqpt_name}: {i} should be greater than 0")
        for i in plus_minus_inputs:
            if int(cur_eqpt[i]) == 0:
                self.errors.append(f"{eqpt_name}: {i} should be greater than or less than 0")
        

if __name__ == "__main__":
    from data import Equipment 
    equipment = Equipment()
    equipment.append(
        {"eqpt_name": "Test1",
         "mounting_location": "Floor",
         'w_p_input': '4',
          's_ds_input': '4',
          'a_p_input': '4',
          'r_p_input': '10',
          'omega_input': '4',
          'z_input':'4',
          'h_input': '4',
          'capital_a_input': '-1',
          'capital_b_input': '4',
         'b_input': '0',
         'a_input': '4', 
         }
    )
    test = InputValidation(equipment)
    test.validate()
    print(test.errors) 
    
