import numpy as np
from scipy import stats
import statistics

'''
Methods for calculating switches in Semantic Foraging methods.
    Current Methods:
        (1) Simdrop: 
        (2) Troyer Norms:
        (3) Multimodal Simdrop:
    
    To do:
        (4) Semantic Scent 
        (5) Delta Similarity

    Output Format: 
        Each switch method should preserve the same length/general format for returing switch values, 
        which can then be used in the foraging models, passed as a parameter

        length: each switch list should be the same length as the fluency_list
        coding: 
            0 - no switch
            1 - switch predicted by method
            2 - boundary case
    
'''


def switch_simdrop(fluency_list, semantic_similarity):
    '''
    
        Args:

        Returns:
    '''
    simdrop = []
    for k in range(len(fluency_list)):
        if (k > 0 and k < (len(fluency_list)-2)): 
            # simdrop
            if (semantic_similarity[k+1] > semantic_similarity[k]) and (semantic_similarity[k-1] > semantic_similarity[k]):
                simdrop.append(1)
            
            else:
                simdrop.append(0)

        else:
            simdrop.append(2)

    return simdrop

def switch_troyer(fluency_list,norms):
    '''
        Args:

        Returns:
    '''
    troyer = []

    for k in range(len(fluency_list)):
        if k > 0:
            item1 = fluency_list[k]
            item2 = fluency_list[k-1]
            category1 = norms[norms['Animal'] == item1]['Category'].values.tolist()
            category2 = norms[norms['Animal'] == item2]['Category'].values.tolist()

            if len(list(set(category1) & set(category2)))== 0:
                troyer.append(1)

            else:
                troyer.append(0)

        else:
            troyer.append(2)
    
    return troyer

def switch_multimodal(fluency_list,semantic_similarity,phonological_similarity,alpha):
    '''
        
        Args:
            fluency_list (list, size = N): fluency list to predict switches on
            semantic_similarity ():
            phonological_similarity ():
            alpha (int): alpha parameter that dictates the weight of semantic vs. phonological cue

        Returns:
    '''    
    #Check if alpha is between 0 and 1
    
    if alpha > 1 or alpha < 0:
        raise Exception("Alpha parameter must be within range [0,1]")
    simphon = alpha * np.array(semantic_similarity) + (1 - alpha) * np.array(phonological_similarity)
    multimodalsimdrop = []

    for k in range(len(fluency_list)):
        if (k > 0 and k < (len(fluency_list) - 2)): 
            if (simphon[k + 1] > simphon[k]) and (simphon[k - 1] > simphon[k]):
                multimodalsimdrop.append(1)
            else:
                multimodalsimdrop.append(0)

        else:
            multimodalsimdrop.append(2)

    return multimodalsimdrop

# def switch_semanticscent():
#     '''
#         TODO : Implement Semantic Scent Switch Method
        
#         Args:

#         Returns:
#     '''
def switch_delta(fluency_list, semantic_similarity, rise_thresh, fall_thresh):
    '''
        TODO: Implement Delta Switch Method
        Args:

        Returns:
    '''
    if rise_thresh > 1 or rise_thresh < 0:
        raise Exception("Rise Threshold parameter must be within range [0,1]")

    if fall_thresh > 1 or fall_thresh < 0:
        raise Exception("Fall Threshold parameter must be within range [0,1]")

    switchVector = [2] # first item designated with 2

    # obtain consecutive semantic similarities b/w responses
    # z-score similarities within participant
    similaritiesZ = stats.zscore(semantic_similarity[1:])
    medianSim = statistics.median(similaritiesZ)
    meanSim = 0
    similaritiesZ = np.concatenate(([np.nan], similaritiesZ))

    # define subject level threshold = median (zscored similarities)
    # firstSwitchSimThreshold = meanSim
    firstSwitchSimThreshold = medianSim
    # for second item, if similarity < median, then switch, else cluster
    if similaritiesZ[1] < firstSwitchSimThreshold:
        switchVector.append(1)
    else:
        switchVector.append(0)

    currentState = switchVector[1]
    previousState = currentState

    # for all other items:
    for n in range(1,len(fluency_list)-1):
    #   consider n-1, n, n+1 items
        
        simPrecedingToCurrentWord = similaritiesZ[n]
        
        simCurrentToNextWord = similaritiesZ[n+1]
        if previousState == 0: #if previous state was a cluster
            if fall_thresh < (simPrecedingToCurrentWord - simCurrentToNextWord): # similarity diff fell more than threshold
                currentState = 1 # switch
            else:
                currentState = 0 # cluster
        else: # previous state was a switch
            if rise_thresh < (simCurrentToNextWord - simPrecedingToCurrentWord): # similarity diff is greater than our rise threshold
                currentState = 0 # cluster
            else:
                currentState = 1 # switch

        switchVector.append(currentState)
        previousState = currentState

    return switchVector
