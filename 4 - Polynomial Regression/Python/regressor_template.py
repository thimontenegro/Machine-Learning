# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:17:31 2019

@author: Thiago Montenegro
"""

#Regressor Template
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

#Spliotting the dataset into the Training set and Test Set
"""
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)
"""

#Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)
""" 

#Fitting the Regression Model to the dataset
#create your regressor here

#Comparing Linear Regression vs Polynomial Regression

from sklearn.linear_model import LinearRegression
#Fitting the Regression Model to the dataset
linear_regressor = LinearRegression()


#Predicting a new Result with Linear Regression


#Predicting a new Result with Polynomial Regression
y_pred = regressor.predict([[6.5]])

#Visualising the Regression Results
plt.scatter(X,Y, color = 'blue')
plt.plot(X,regressor.predict(X), color = 'black')
plt.xlabel("Position Levels")
plt.ylabel('Salary')
plt.title('Truth or Bluff (Regression Model)')
plt.show()

#Visualising the Regression results(fir higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
#Visualising the Polynomial Regression Results
plt.scatter(X,Y, color = 'blue')
plt.plot(X_grid,regressor.predict(X_grid), color = 'black')
plt.xlabel("Position Levels")
plt.ylabel('Salary')
plt.title('Truth or Bluff (Regression Model)')
plt.show()
