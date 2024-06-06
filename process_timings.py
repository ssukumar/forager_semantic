import os
import pandas as pd
import numpy as np

def split_subject_column():
    
    category_list = ['ANIMALS','BODY PARTS', 'FRUITS', 'HOBBIES', 'HOME APPLIANCES', 'LIQUIDS', 'MEANS OF TRANSPORT', 'MEDICAL CONDITIONS', 'MUSICAL INSTRUMENTS', 'OCCUPATIONS', 'TOOLS', 'VEGETABLES']
    forager_suffix = "_outputs_forager_results"
    lexical_file = "lexical_results.csv"
    output_dir = "output_timing"
    
    op_csv = "lexical_data_corrected.csv"
    
    for categ in category_list:
        print(categ)
        fn = os.path.join(output_dir, categ+forager_suffix, lexical_file)
        op_df = pd.read_csv(fn, header= 0)
        op_df["IRT"] = np.nan
        for ix in op_df.index:
            op_df.at[ix, 'Subject'] = eval(op_df.at[ix, 'Subject'])
            op_df.at[ix, 'IRT'] = op_df.at[ix, 'Subject'][1]
            op_df.at[ix, 'Subject'] = op_df.at[ix, 'Subject'][0]
        
        print(output_dir)
        op_csv_fn = os.path.join(output_dir, categ+forager_suffix, op_csv)
        op_df.to_csv(op_csv_fn, header = True, index=False)
        print(f"Saved file to {op_csv_fn}")
        

if __name__=='__main__':
    split_subject_column()