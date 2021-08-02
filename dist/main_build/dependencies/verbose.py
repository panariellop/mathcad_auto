"""
Gives verbose version of the argument 
"""

def inputs(cur_input):
    conversion = {
        'eqpt_name': 'Equipment Name',
        'project_number': "Project Number", 
        "tags": "Equipment Tags",
        "eqpt_number":"Equipment ID",
        "mounting_location": "Mounting Location", 
        "w_p_input": "W\u209A",
        "s_ds_input": "S_DS",
        "a_p_input": "a_P",
        "r_p_input":"R\u209A",
        'i_p_input':"I\u209A", 
        "omega_input": "Omega\u2080",
        "z_input":"z",
        "h_input":"h",
        "capital_a_input":"A",
        "capital_b_input":"B",
        "a_input":"a",
        "b_input":"b",
        "capital_h_input":"H",
        "cg_factor_input":"CG factor",
        "cgz_factor_input":"CG z.factor",
        "h_1_input":"h\u2081", 

    }
    try:
        return conversion[cur_input]
    except:
        #in case the conversion is not listed here 
        return cur_input 

def outputs(cur_output):
    conversion = {
        'z_h_output': "z\u2095",
        'cgy_output': "CGy",
        'cgx1_output': 'CGx\u2081',
        'cgx2_output': 'CGx\u2082',
        't_max_1_output': 'Tmax\u2081',
        't_max_2_output': 'Tmax\u2082',
        }
    #convert, but if not then just return the output back 
    try: return conversion[cur_output]
    except: return cur_output
if __name__ == "__main__":
    pass
