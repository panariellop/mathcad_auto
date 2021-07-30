class InputValidation():
    """
    Validate the following inputs:
    1) Mounting Location 
    2) 
    """
    def __init__(self, cur_input):
        self.cur_input = cur_input 
    def mounting_location(self, files)->bool:
        """
        Can have the following 
        """
        if files.templates[self.cur_input]:
            #Check if the mounting location is in the templates
            return True
        else:
            return False 
        

if __name__ == "__main__":
    pass
