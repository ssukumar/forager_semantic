import csv
import itertools
from create_lexical_data import data
import argparse


def create_list(filepath):
    
    file = open(filepath, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close
    
    words = list(itertools.chain(*data))
    
    
    return words
    
    
if __name__ == "__main__":

    
    # fp = "data/lexical_data/vocab_appliances.csv"
    parser = argparse.ArgumentParser(description='Execute Semantic Foraging Code.')
    parser.add_argument('--vocab_fp', type=str,  help='specifies path to vocab lists')
    parser.add_argument('--category', type=str,  help='specifies category name')
    args = parser.parse_args()
    
    words = create_list(args.vocab_fp)
    data(words, args.category)