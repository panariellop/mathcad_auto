import unittest 
import csv 
from main import * 
unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1 #performs tests in order 
def get_eqpt():
    file = 'C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template.xlsx'
    return get_eqpt_from_xl(file)

class TestMathcad(unittest.TestCase):

    def test_get_eqpt_from_xl(self):
        #1) get the template file 
        #2) Count the number of items in the equipment object produced 
        equipment = get_eqpt()
        self.assertTrue((len(equipment.items) > 0), "No equipment were found in the excel file  by calling get_eqpt_from_xl")

    def test_mathcad_calcuate(self):
        #1) Get the equipment 
        equipment = get_eqpt()
        #2) Get the template file 
        template_file = "C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template_document_mathcad_7.mcdx"
        returned_dict = mathcad_calculate(equipment, template_file)
        len_dict = 0 
        for key, val in returned_dict.items():
            len_dict +=1
        self.assertTrue(len_dict > 0, "The dictionary returned by mathcad_calculate was empty.")

    def test_generate_report(self):
        #need to test if one report file is generated, the database csv file is generated with the new entry
        #cleanup files generated (mathcad file, csv file)
        equipment = get_eqpt()
        files = SelectTemplates()
        files.templates = {'Wall, Floor': 'C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template_document_mathcad_7.mcdx', 'Floor': 'C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template_document_mathcad_7.mcdx', 'Wall': 'C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template_document_mathcad_7.mcdx', 'Ceiling': 'C:/Users/Owner/Desktop/mathcad_auto/templates/starter_template_document_mathcad_7.mcdx'}
        properly_generated = pre_generate_report(equipment, files)
        self.assertTrue(properly_generated, "Report not generated properly")

        #test if the file was actually generated 
        import os 
        num_files = 0 
        for base, dirs, the_files in os.walk("C:/Users/Owner/Desktop/mathcad_auto/dist/mathcad_automation_output"): 
            for f in the_files:
                num_files +=1 
        self.assertTrue(num_files>1, "There are not the expected number of files in the output directory")

        database = "./mathcad_automation_output/all_mathcad_reports.csv"
        csv_line_count = 0
        with open(database, mode="r") as f:
            csv_reader = csv.DictReader(f)
            for line in csv_reader:
                csv_line_count += 1 
        #we excpet 2 lines in the csv file: header and 1 data line 
        self.assertTrue(csv_line_count>0, "Report not saved to csv file" )

        #remove output folder   
        import shutil
        shutil.rmtree("C:/Users/Owner/Desktop/mathcad_auto/dist/mathcad_automation_output")




if __name__ == "__main__":
    print("---------Testing Various Functions---------")
    unittest.main()
    print("---------Finished Testing---------")