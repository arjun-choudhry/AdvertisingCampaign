# -*- coding: utf-8 -*-
"""
@author: arjun
"""
#%reset -f
# ****************************************************************************************************************
# Optimizing the click-through-rate of different users for ads in a social network
# ****************************************************************************************************************

# importing the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# RANDOM SELECTION
# We will first check the total reward for the random selection. ie we will not apply any algorithm and will randomly select the add and check the reward for it. Then we will use it to compare with the result when we apply the ucb algorithm.
import random
observations = len(dataset)
d=10
totalReward = 0
ads_selected = []
for i in range(0,observations):
    randnumber = random.randrange(d)
    ads_selected.append(randnumber)
    roundReward = dataset.values[i,randnumber]
    totalReward = totalReward + roundReward

# Plotting a histogran to visualize results
plt.hist(ads_selected)
plt.title('Histograms of ads selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

# So, total reward comes to 1264. Also, all the ads are selected almost equally. We can see this using the histogram