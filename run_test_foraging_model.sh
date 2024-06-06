#!/bin/bash

#GROUP A
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/ANIMALS_outputs.csv" --category "ANIMALS" --pipeline switches --switch norms_associative
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/HOME APPLIANCES_outputs.csv" --category "HOME APPLIANCES" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/BODY PARTS_outputs.csv" --category "BODY PARTS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/FRUITS_outputs.csv" --category "FRUITS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/HOBBIES_outputs.csv" --category "HOBBIES" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/HOLIDAYS_outputs.csv" --category "HOLIDAYS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/MUSICAL INSTRUMENTS_outputs.csv" --category "MUSICAL INSTRUMENTS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/LIQUIDS_outputs.csv" --category "LIQUIDS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/MEDICAL CONDITIONS_outputs.csv" --category "MEDICAL CONDITIONS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/OCCUPATIONS_outputs.csv" --category "OCCUPATIONS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/TOOLS_outputs.csv" --category "TOOLS" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/MEANS OF TRANSPORT_outputs.csv" --category "MEANS OF TRANSPORT" --pipeline models --model dynamic --switch simdrop
# python run_foraging.py --data "data/fluency_lists/test_hand_corrected/VEGETABLES_outputs.csv" --category "VEGETABLES" --pipeline models --model dynamic --switch simdrop

# GROUP B
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/OFFICE SUPPLIES_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "OFFICE SUPPLIES"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/ACCOMODATIONS_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "ACCOMODATIONS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/COUNTRIES_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "COUNTRIES"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/FLOWERS_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "FLOWERS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/FOODS_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "FOODS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/FURNITURE_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "FURNITURE"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/THINGS FOUND IN KITCHENS_outputs.csv" --pipeline models --model dynamic --switch simdrop --category "THINGS FOUND IN THE KITCHEN"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/NATURAL ENVIRONMENT_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "NATURAL ENVIRONMENTS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/SPORTS_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "SPORTS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/NON-FOOD ITEMS FOUND IN SUPERMARKET_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "NON-FOOD ITEMS FOUND IN SUPERMARKET"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/TECHNOLOGY GADGETS & DEVICES_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "TECHNOLOGY GADGETS AND DEVICES"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/TOYS_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "TOYS"
python run_foraging.py --data "data/fluency_lists/test_hand_corrected/CLOTHING_outputs.csv" --pipeline  models --model dynamic --switch simdrop --category "CLOTHING"
