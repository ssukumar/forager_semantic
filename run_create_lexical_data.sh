#!/bin/bash

echo "CREATING LEXCIAL DATA FOR ALL CATEGORIES"

# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_appliances.csv" --category "HOME APPLIANCES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_office_supplies.csv" --category "OFFICE SUPPLIES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_accomodations.csv" --category "ACCOMODATIONS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_body_parts.csv" --category "BODY PARTS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_countries.csv" --category "COUNTRIES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_flowers.csv" --category "FLOWERS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_foods.csv" --category "FOODS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_fruits.csv" --category "FRUITS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_furniture.csv" --category "FURNITURE"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_hobbies.csv" --category "HOBBIES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_holidays.csv" --category "HOLIDAYS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_instruments.csv" --category "MUSICAL INSTRUMENTS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_kitchen.csv" --category "THINGS FOUND IN THE KITCHEN"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_liquids.csv" --category "LIQUIDS"
python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_medical_conditions.csv" --category "MEDICAL CONDITIONS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_natural_environments.csv" --category "NATURAL ENVIRONMENTS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_occupations.csv" --category "OCCUPATIONS"
python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_sports.csv" --category "SPORTS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_supermarket.csv" --category "NON-FOOD ITEMS FOUND IN SUPERMARKET"
python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_technology.csv" --category "TECHNOLOGY GADGETS AND DEVICES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_tools.csv" --category "TOOLS"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_toys.csv" --category "TOYS"
python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_transport.csv" --category "MEANS OF TRANSPORT"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_vegetables.csv" --category "VEGETABLES"
# python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_clothing.csv" --category "CLOTHING"


# categories = ('OFFICE SUPPLIES' 'TECHNOLOGY GADGETS & DEVICES' 'NON-FOOD ITEMS FOUND IN SUPERMARKET' 'THINGS FOUND IN KITCHENS' 'FOODS' 'CLOTHING' 'FLOWERS' 'TOYS' 'SPORTS' 'FURNITURE' 'COUNTRIES' 'ACCOMODATIONS' 'NATURAL ENVIRONMENT')
#
#
# for str in ${categories}; do
# 	python3.11 run_create_lexical_data.py --vocab_fp "data/lexical_data/vocab_appliances.csv" --category "HOME APPLIANCES"
# done