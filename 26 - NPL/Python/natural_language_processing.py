# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:00:49 2019

@author: Thiago Montenegro
"""
#Natural Language Processing

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset

dataset = pd.read_csv('Data/Restaurant_Reviews.tsv', delimiter = '\t' , quoting = 3)

#Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = [] # Collections of texts
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

#Creating a Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer  
cv = CountVectorizer(max_features = 1500 )
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[: , 1].values

#Fitting and training
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.20, random_state = 0)



#Fitting NPL into Naive Bayes
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
#Predicint the test set results
y_pred = classifier.predict(X_test)
#Making the confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
positives_percentage = accuracy_score(y_test, y_pred)
