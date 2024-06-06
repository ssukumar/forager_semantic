import pandas as pd
import numpy as np
import os
import argparse

def augment_vocab(fluency_list, vocab_file):
    
    fluency_df = pd.read_table(fluency_list, header= 0)
    word_recalled = np.unique(fluency_df['Word']).tolist()
    
    vocab_df = pd.read_csv(vocab_file, header = None)
    vocab_list = vocab_df[0].tolist()
    words_excluded = list(set(word_recalled) - set(vocab_list))
    vocab_list += words_excluded
    
    vocab_df = pd.DataFrame(vocab_list)
    vocab_df.to_csv(vocab_file, header=False, index=False)
    
    
def main(fluency_dir, vocab_dir):
    
    # categories = ['ACCOMODATIONS', 'ANIMALS', 'BODY PARTS', 'CLOTHING', 'COUNTRIES', 'FLOWERS', 'FOODS', 'FRUITS', 'FURNITURE', 'HOBBIES', 'HOLIDAYS', 'HOME APPLIANCES', 'LIQUIDS',
#     'MEANS OF TRANSPORT', 'MEDICAL CONDITIONS', 'MUSICAL INSTRUMENTS', 'NATURAL ENVIRONMENT', 'NON-FOOD ITEMS FOUND IN SUPERMARKET', 'OCCUPATIONS', 'OFFICE SUPPLIES', 'SPORTS',
#     'TECHNOLOGY GADGETS & DEVICES', 'THINGS FOUND IN KITCHENS', 'TOOLS', 'TOYS', 'VEGETABLES']
    
    categories = ['ANIMALS','BODY PARTS', 'FRUITS', 'HOBBIES', 'HOLIDAYS', 'HOME APPLIANCES', 'LIQUIDS', 'MEANS OF TRANSPORT', 'MEDICAL CONDITIONS', 'MUSICAL INSTRUMENTS', 'OCCUPATIONS', 'TOOLS', 'VEGETABLES']
    
    # fluency_dir = os.path.join('data', 'fluency_lists')
    # vocab_dir = os.path.join('data', 'lexical_data')
    
    for category in categories:
        
        print(f"CATEGORY: {category}\n\n")
        
        categ_lc = category.lower()
        categ_lc = categ_lc.replace(' ', '_')
        vocab_file = os.path.join(vocab_dir, 'vocab_'+categ_lc+'.csv')
        fluency_file = os.path.join(fluency_dir, category+'_outputs.csv')
        augment_vocab(fluency_file, vocab_file)
        
        
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Execute Semantic Foraging Code.')
    parser.add_argument('--fluency_path', type=str,  help='specifies path to fluency lists')
    parser.add_argument('--vocab_dir', type=str,  help='specifies vocab directory')
    args = parser.parse_args()
    main(args.fluency_path, args.vocab_dir)