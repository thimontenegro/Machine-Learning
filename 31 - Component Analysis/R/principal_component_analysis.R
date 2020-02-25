dataset = read.csv('Data/Wine.csv')

#Splitting the dataset into training set and test set
library(caTools)
set.seed(123)
split = sample.split(dataset$Customer_Segment, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Feature Scaling
training_set[-14] = scale(training_set[, -14])
test_set[-14] = scale(test_set[, -14])

#Applying PCA
library(caret)
library(e1071)
pca = preProcess()