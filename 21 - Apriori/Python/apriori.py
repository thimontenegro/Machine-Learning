# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 02:19:18 2019

@author: Thiago Montenegro
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data/Market_Basket_Optimisation.csv', header = None)

transactions = []

for i in range(0, len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

#Training Apriori On the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003 , min_confidence = 0.4, min_lift =3 , min_length = 2)
#Support calculus
#products whichj is purchased 3 products by day 
# 3 * 7 / total number_of_transactions


#Visualising the transactions
results = list(rules)
