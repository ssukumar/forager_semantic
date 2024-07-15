

## Running the forager toolbox for analysis

Here, we will be working with the forked version of the `forager` toolbox.
Original Repo: https://github.com/thelexiconlab/forager
Forked Repo: 

1. Make sure to create lexical data by running the shell script `run_create_lexical_data.sh` using the following command :
> sh run_create_lexical_data.sh

This file should create the relevant files of identifying frequency and semantic similarity from the vocabularies for each categories.

2. Make sure the grouped data files are under `data/fluency_lists`. [NOTE: if working with a subset of data, store the corresponding data under a different folder. Here i have stored the hand corrected under ` `]

3. Run the main foraging code (refer to the instructions in the original repository for what you want the forager to do).
   
   * For instance if you want to just get lexical information for the fluency lists (frequency, semantic similarity), run the script `run_foraging.sh`.  NOTE: make sure before running this script that the. correct lines are uncommented based on the fluency lsits you want to run.
   
   * If you want to run the full model and switches, then run the shell script `run_foraging_model.sh`
   
   * If you want to run the lexical information, or, full model and switches on the hand corrected subset of data alone, run the shell script `run_test_foraging.sh` or `run_test_foraging_model.sh`, respectively. 
   
4. The outputs of forager are stored in output folder. 

5. The relevant output compressed file needs to be extracted and tranferred back to the 'Semantic_Data_Analysis' repository, where it can be analyzed using the R files.