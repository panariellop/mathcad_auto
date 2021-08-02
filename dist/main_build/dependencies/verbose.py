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

if __name__ == "__main__":
    pass
