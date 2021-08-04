"""
Gives verbose version of the argument (more readable version)
ex: h_1_input -> h1
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
        't_u1_output': "Tu\u2081 - Direction X",
        't_u2_output': "Tu\u2082 - Direction Y",
        't_u12_output': "Tu\u2081 - Direction X",
        't_u12_output': "Tu\u2082 - Direction Y",
        }
    #convert, but if not then just return the output back 
    try: return conversion[cur_output]
    except: return cur_output


def is_asd_output(output:str)->bool:
    allowed = [
        't_max_1_output',
        't_max_2_output'
    ]
    if output in allowed: return True
    else: return False 

def is_lrfd_output(output:str)->bool:
    allowed = [
        't_u1_output',
        't_u2_output',
        't_u12_output',
        't_u12_output',
    ]
    if output in allowed: return True 
    else: return False 
if __name__ == "__main__":
    pass
