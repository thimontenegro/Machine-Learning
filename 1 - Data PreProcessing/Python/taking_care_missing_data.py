# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 04:32:16 2019

@author: Thiag
"""

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X[:,1:3]) #Upperbound excluded! 1-2
X[:, 1:3]  = imputer.transform(X[:, 1:3] )
