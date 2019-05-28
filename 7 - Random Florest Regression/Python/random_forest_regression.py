# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:19:00 2019

@author: Thiago Montenegro
"""

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X,y)

#Predicting a new result
y_pred = regressor.predict([[6.5]])

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid),1))
#Visualising the Polynomial Regression Results
plt.scatter(X,y, color = 'blue')
plt.plot(X_grid,regressor.predict(X_grid), color = 'black')
plt.xlabel("Position Levels")
plt.ylabel('Salary')
plt.title('Truth or Bluff (Random Forest Regression)')
plt.show()
