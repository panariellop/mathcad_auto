"""
Gives verbose version of the argument 
"""

def verbose_input(cur_input):
    conversion = {
        "tags": "Equipment Tags",
        "eqpt_number":"Equipment ID",
        "mounting_location": "Mounting Location", 
        "w_p_input": "W_p",
        "s_ds_input": "S_DS",
        "a_p_input": "a_P",
        "r_p_input":"R_p",
        "omega_input": "Omega_0",
        "z_input":"z",
        "h_input":"h",
        "capital_a_input":"A",
        "capital_b_input":"B",
        "a_input":"a",
        "b_input":"b",
        "capital_h_input":"H",
        "cg_factor_input":"CG_factor",
        "cgz_factor_input":"CG_z.factor",
        "h_1_input":"h1", 

    }
    try:
        return conversion[cur_input]
    except:
        #in case the conversion is not listed here 
        return cur_input 

if __name__ == "__main__":
    pass
