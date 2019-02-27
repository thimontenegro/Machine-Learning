# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:25:05 2019

@author: Thiag
"""

#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset

database = pd.read_csv('Data.csv')
#matrix of features
X = database.iloc[:, :-1].values
#No database, pegar todas as linhas e e todas colunas exceto a ultima
Y = database.iloc[:,3].values

"""
#Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X[:,1:3]) #Upperbound excluded! 1-2
X[:, 1:3]  = imputer.transform(X[:, 1:3] )

#Encoding Categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

label_encoder_X = LabelEncoder()
X[:,0] = label_encoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
label_encoder_Y = LabelEncoder()
Y = label_encoder_Y.fit_transform(Y)
"""

#Splitting the data into Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y , 
                                                    test_size = 0.2,
                                                    random_state = 0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)