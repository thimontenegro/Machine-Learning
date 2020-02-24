# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:53:18 2019

@author: Thiago Montenegro
"""

#Data 1' - Pre processing the Data
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importind the dataset
dataset = pd.read_csv('Data/Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

#Enconding the categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelenconder_X_1 = LabelEncoder()
X[:, 1] = labelenconder_X_1.fit_transform(X[:, 1])
#For gender!
labelenconder_X_2 = LabelEncoder()
X[:, 2] = labelenconder_X_2.fit_transform(X[:, 2])
#Avoiding dummy variable trap
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

#Splitting the dataset into the Training set and test set
from sklearn.model_selection import train_test_split
X_train,  X_test, y_train, y_test = train_test_split(X,
                                                     y,
                                                     test_size = 0.25,
                                                     random_state = 42)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Importing Artificial Neural Networks libraries
import keras
from keras.models import Sequential #Initialize Neural Network
from keras.layers import Dense #Create layers of Neural Network

#Initilising the Neural Network
classifier = Sequential()#Future Neural Network

#Adding the input layer and the first layer
#Output_dim TIP = Avarage of Input nodes Layers and OutputNodes layers = (11 + 1)/2
#1 For output node is because our output is a binary!
classifier.add(Dense(units = 6, kernel_initializer = 'uniform',
                     activation = 'relu', input_dim = 11))

#Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform',
                     activation = 'relu'))

#Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform',
                     activation = 'sigmoid'))
 
#Compiling the ANN
classifier.compile(optimizer = 'adam', 
                   loss = 'binary_crossentropy',
                   metrics = ['accuracy']
                   )
#Fitting the ANN to the Training Set
classifier.fit(X_train, y_train,
               batch_size = 10,
               epochs = 100)


#Predicting the Results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)
#Making the confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
