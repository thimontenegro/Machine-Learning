# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 05:19:32 2019

@author: Thiag
"""
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
years_experience = dataset.iloc[:,:-1].values
salary = dataset.iloc[:,1].values

#Splitting the dataset into the training set and Test st
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train,Y_test = train_test_split(years_experience,
                                                     salary, test_size =1/3,
                                                     random_state = 0)

#Fitting Simple Linear Regression to Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#Predicting the Test set result
y_pred = regressor.predict(X_test)
x_train_pred = regressor.predict(X_train)
#Visualising the training set results
plt.scatter(X_train,Y_train, color = 'red') #Real salaries
#plot the regression line
#plot the predicions of training
"""
Predict the real salaries with the predicted salaries
"""
plt.plot(X_train, x_train_pred, color = 'blue')
plt.title("Salary vs Experience (Training Set)")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show() #End of graphic


#Visualising the Test Set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
