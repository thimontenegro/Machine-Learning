# Multiple Linear Regression

#Importing the dataset
dataset = read.csv('50_Startups.csv')
#Enconding categorical data
dataset$State = factor(dataset$State, 
                       levels = c('New York', 'Florida', 'California'),
                       labels = c(1,2,3))

#Spliting the dataset into the training set and Test Set
#install.packages('caTools')
library(caTools)
set.seed(123)

split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting Multiple Linear Regression to the Training Set
#Formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State
#Or
#Formula = Profit ~ . 
regressor = lm(formula = Profit ~ .,
               data = training_set)

