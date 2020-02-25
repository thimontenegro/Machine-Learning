# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:50:14 2019

@author: Thiago Montenegro
"""
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
#Importing the dataset
dataset = pd.read_csv('Data/Ads_CTR_Optimisation.csv')

#Implementing random selection
def random_selection():
    import random
    N = 10000
    d = 10
    ads_selected = []
    total_reward = 0
    for n in range(0, N):
        ad = random.randrange(d)
        ads_selected.append(ad)
        reward = dataset.values[n, ad] 
        total_reward = total_reward + reward
    
    #Visualising the results - Histogram
    plt.hist(ads_selected)
    plt.title('Histogram of ads selections')
    plt.xlabel('Ads')
    plt.ylabel('Number of times each ad was selected')
    plt.show()

#Implementing Upper Bound Confidence
N = len(dataset)
d = 10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_reward = [0] * d
total_reward = 0
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if(numbers_of_selections[i] > 0): 
            avarage_reward = sums_of_reward[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = avarage_reward + delta_i
        else:
            upper_bound = 1e400
        if(upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_reward[ad] = sums_of_reward[ad] + reward
    total_reward = total_reward + reward
    
#Visualising the Results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
    