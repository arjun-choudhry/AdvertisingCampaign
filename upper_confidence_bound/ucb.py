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
totalReward_randomrd = 0
ads_selected_random = []
for i in range(0,observations):
    randnumber = random.randrange(d)
    ads_selected_random.append(randnumber)
    roundReward = dataset.values[i,randnumber]
    totalReward_randomrd = totalReward_randomrd + roundReward

# Plotting a histogran to visualize results
plt.hist(ads_selected_random)
plt.title('Histograms of ads selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

# So, total reward comes to 1264. Also, all the ads are selected almost equally. We can see this using the histogram

# Now, we will use the ucb algorithm to optimize the results
import math
number_of_selections = [0] * d
sum_of_rewards = [0] * d
ads_selected_ucb = []
total_reward_ucb = 0
for n in range(0,observations):
    max_upper_bound = 0
    ad = 0
    for i in range(0,d):
        if(number_of_selections[i] > 0):
            average_reward = sum_of_rewards[i] / number_of_selections[i]
            delta_i = math.sqrt((3/2 * math.log(n+1))/number_of_selections[i])
            upper_confidence_value = average_reward + delta_i
        else:
            upper_confidence_value = 1e400
        if(upper_confidence_value > max_upper_bound):
            max_upper_bound = upper_confidence_value
            ad = i

    ads_selected_ucb.append(ad)
    reward_ucb = dataset.values[n,ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward_ucb
    number_of_selections[ad] = number_of_selections[ad] + 1
    total_reward_ucb = total_reward_ucb + reward_ucb

# Hence, we see that the total reward in this case is 2178