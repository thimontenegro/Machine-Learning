# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:48:47 2019

@author: Thiag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

#Enconding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder = LabelEncoder()
X[:,3] = labelEncoder.fit_transform(X[:,3])
one_hot_encoder = OneHotEncoder(categorical_features = [3])
X = one_hot_encoder.fit_transform(X).toarray()

#Avoiding the Dummy Variable Trap
X = X[:, 1:]
#Splitting the dataset into the Training and Testing
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)

#Fitting multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#Predicting the Results!
predict = regressor.predict(X_test)

#Building the Optimal model Using BackWard Elimination
import statsmodels.formula.api as sm
X = np.append(arr =  np.ones((50, 1)).astype(int), values = X, 
              axis = 1)