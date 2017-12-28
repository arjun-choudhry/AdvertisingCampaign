"""
@author: arjun
"""
#%reset -f
# ****************************************************************************************************************
# Optimizing the click-through-rate of different users for ads in a social network using thompson sampling
# ****************************************************************************************************************

# importing the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# implementing thompson sampling
import random
d = 10
observations = len(dataset)
ads_selected_thompson = []
totalRewards_thompson = 0
number_of_ones_thompson = [0]*d
number_of_zeroes_thompson = [0]*d
for n in range(0,observations):
    ad = 0
    max_randDraw = 0
    for i in range(0,d):
        nOnes = number_of_ones_thompson[i]
        nZeroes = number_of_zeroes_thompson[i]
        randDraw = random.betavariate(nOnes+1,nZeroes+1)
        if(randDraw > max_randDraw):
            max_randDraw = randDraw
            ad = i

    ads_selected_thompson.append(ad)
    reward = dataset.values[n,ad]
    if(reward == 1):
        number_of_ones_thompson[ad] = number_of_ones_thompson[ad] + 1
        totalRewards_thompson = totalRewards_thompson + 1
    else:
        number_of_zeroes_thompson[ad] = number_of_zeroes_thompson[ad] + 1