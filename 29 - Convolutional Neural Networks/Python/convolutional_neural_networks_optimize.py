# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:03:35 2019

@author: Thiago Montenegro 
"""

#Part 1 - Building the Convolutional Neural Network
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
#CNN = CONVOLUTION -> MAX POOLING -> FLATTENING -> FULL CONECTION
#Initialising the CNN
classifier = Sequential()

#Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
 # 32 filters by 3 rows and 3 lines
 
#Step 2 - Max Pooling
classifier.add(MaxPooling2D(pool_size = (2,2))) 
#Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2))) 

#Step 3 - Flatting
classifier.add(Flatten())

#Step 4 - Full Conection
classifier.add(Dense(units = 128, activation = 'relu'))


classifier.add(Dense(units = 1, activation = 'sigmoid'))

#Compiling 
classifier.compile(optimizer = 'adam',
                   loss = 'binary_crossentropy',
                   metrics = ['accuracy'])

#Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'Data/dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'Data/dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000, #number of images on training set
        epochs=1,
        validation_data= test_set,
        validation_steps=2000) # number of images on test set