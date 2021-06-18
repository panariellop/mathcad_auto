import datetime as date 
import csv 
import time
import os 
import stat 
import dateutil.parser as parser

def parse_eqpt():
    #get all the names of the eqpt, all the mounting locations, file name, date which it was saved 
    #get all files in dir 
    filenames = os.listdir(os.getcwd())
    filtered_files = list()
    for f in filenames:
        if "." in f and f.split('.')[-1] == "mcdx":
            file_stat = os.stat(f)
            #gets te time in which the file was last modified
            modified_time = parser.parse(time.ctime(file_stat[stat.ST_MTIME]))
            modified_time = modified_time.isoformat()
            filtered_files.append([f, modified_time])
    print(filtered_files)




def save_eqpt_to_csv(values, filepath, unique_report_name):
    cur_date = date.today()
    try:
        with open(filepath, "a", newline = "") as f:
            csv_writer = csv.writer(f)
            try:
                new_row = [
                    cur_date, 
                    values['tags'].upper(), 
                    values['eqpt_name'].upper(),
                    values['mounting_location'].upper(),
                    unique_report_name,
                ]
            except:
                print("Equipment name, mounting location, and tags must all be included")
            csv_writer.writerow(new_row)
        f.close()
        return True 
    except: 
        return False 



if __name__ == "__main__":
    parse_eqpt()
