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