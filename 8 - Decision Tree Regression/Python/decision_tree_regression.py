# -*- coding: utf-8 -*-
"""
Created on Sat May 25 10:25:51 2019

@author: Thiag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values #matriz de valores
y = dataset.iloc[:,  2].values #nosso target

#Fitting the Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 42)
regressor.fit(X, y)

#Predicting a new result
y_pred = regressor.predict([[6.5]])

#Visualiing the Decision Tree Regression Results
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X,y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()