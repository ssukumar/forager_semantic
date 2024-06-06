#Adapted from Kumar et al (2022); uses NGRAMS with REST API to obtain frequencies

import urllib
import requests
import pandas as pd
from tqdm import tqdm
import numpy as np
# from string import punctuation
import re
import os

def get_frequencies(embeddings,path_for_lexical_data):
    '''
        Description:
            Creates a CSV file of frequencies for each word in the vocabulary, obtained from the Google Books Ngram Dataset (version 2)
            The first column is the word, the second is the log count, and the third is the raw count.
            The resulting file is saved in the data/lexical data folder.
        Args:
            (1) embeddings: path to the CSV file of semantic embeddings
    '''
    data = pd.read_csv(embeddings) 
    items = data.columns.to_list()
    # print(items)
    items_and_counts = []
    for item in tqdm(items):
        query = item.replace(" ", "+")
        print("QUERY = "+query)d
        # encoded_query = urllib.parse.quote(new)'
        base_url = 'https://api.ngrams.dev'
        corpus = 'eng'
        params = {'query': query, 'flags' : 'cr'}
        print(params)
        params_str = '&'.join('{}={}'.format(name, value) for name, value in params.items())
        urll =os.path.join(base_url, corpus, 'search?'+params_str)
        print("search URL: "+ urll)
        response = requests.get(urll).json()
        print(response)
        # response_flat = re.split('\n|\t',response.text)[:-1]        
        # print(response_flat)
        # response_table = pd.DataFrame(np.reshape(response_flat, newshape=(-1,7))).iloc[:,:2]
#         response_table.columns = ['word','count']
#         response_table['word'] = response_table['word'].apply(lambda x: re.sub('_0','', x))

        if 'ngrams' in response:
            if not response['ngrams']:
                count = 0
                
            else:
                count = response['ngrams'][0]['absTotalMatchCount']
            
        else:
            count = 0
            
        items_and_counts.append((item, count))
    
    item_counts_df = pd.DataFrame(items_and_counts, columns=['item','count'])
    item_counts_df['count'] = item_counts_df['count'].astype(float)
    item_counts_df.loc[item_counts_df['count'] == 0, 'count'] = 1
    item_counts_df['log_count'] = item_counts_df['count'].apply(np.log10)
    # if log_count is 0, then set to .0001
    item_counts_df.loc[item_counts_df['log_count'] == 0, 'log_count'] = .0001
    item_counts_df = item_counts_df[['item', 'log_count', 'count']]

    #print(item_counts_df)
    item_counts_df.to_csv(path_for_lexical_data + '/USE_frequencies.csv', index=False, header=None)
    return None