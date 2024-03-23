#!/bin/bash

echo "CREATING LEXCIAL DATA FOR ALL CATEGORIES"

python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_appliances.csv" --category "HOME APPLIANCES"