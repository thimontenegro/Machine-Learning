# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:49:01 2019

@author: Thiago Montenegro
"""

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Data/Mall_Customers.csv')
X = dataset.iloc[:, [3,4]].values


#Plot the Dendagram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title("Dendrogram")
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

#We find that optimial number os clusters is 5!

#Fitting hierarchical clustering to the mall dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5,
                             affinity = 'euclidean',
                             linkage = 'ward')
y_hc = hc.fit_predict(X)

#Plot/Visualising the Hierarchical clustering
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 75, c= 'red',label='Careful')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 75, c= 'blue', label='Standard')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 75, c= 'green', label='Target')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 75, c= 'purple', label='Careless')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 75, c= 'pink', label='Sensible')
plt.title('Cluster of clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

