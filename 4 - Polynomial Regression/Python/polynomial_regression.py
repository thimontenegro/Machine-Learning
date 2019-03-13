# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:27:08 2019

@author: Thiago Montenegro
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, 2].values

plt.plot(dataset)
"""
Comparing Linear Regression vs Polynomial Regression
"""
from sklearn.linear_model import LinearRegression
#Fitting linear regression to the dataset

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)

#Fitting Polynomial Regression to the dataset
from sklearn.b  import PolynomialFeatures
polynomial_regressor = PolynomialFeatures(degree = 10)
X_polynomial  = polynomial_regressor.fit_transform(X)
linear_regressor_2 = LinearRegression()
linear_regressor_2.fit(X_polynomial,Y)

#Visualising the Linear Regression results

plt.scatter(X,Y, color = 'red')
plt.plot(X, linear_regressor.predict(X), color = 'black')
plt.xlabel('Position Levels')
plt.ylabel('Salary')
plt.title('Levels vs Salary (Linear Model)')
plt.show()
#Visualising the Polynomial Regression Results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X,Y, color = 'blue')
plt.plot(X_grid,linear_regressor_2.predict(polynomial_regressor.fit_transform(X_grid)), color = 'black')
plt.xlabel("Position Levels")
plt.ylabel('Salary')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.show()

#Predicting a new Result with Linear Regression
linear_regressor.predict([[6.5]])

#Predicting a new Result with Polynomial Regression
linear_regressor_2.predict(polynomial_regressor.fit_transform([[6.5]]))