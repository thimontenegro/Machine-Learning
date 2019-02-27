# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 04:32:48 2019

@author: Thiag
"""

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

label_encoder_X = LabelEncoder()
X[:,0] = label_encoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
label_encoder_Y = LabelEncoder()
Y = label_encoder_Y.fit_transform(Y)
