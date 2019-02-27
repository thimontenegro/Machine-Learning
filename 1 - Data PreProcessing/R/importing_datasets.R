#Data Preprocessing

#Import the dataset
datasets = read.csv(file.choose()) #Data.csv
datasets = datasets[,2:3] #specfic tables
#Taking care of missing data
# datasets$Age = ifelse(is.na(datasets$Age), 
#                       ave(datasets$Age, FUN = function(x) mean(x,na.rm='True')),
#                         datasets$Age)
#                       #taking age column
# #If is missing in datasets age
# 
# #For Salay
# datasets$Salary = ifelse(is.na(datasets$Salary),
#                         ave(datasets$Salary, FUN = function(x) mean(x, na.rm='True')),
#                             datasets$Salary)
# 
# #Encoding Categorical data
# datasets$Country = factor(datasets$Country,
#                           levels = c('France','Spain','Germany'),
#                           labels = c(1,2,3))
# 
# datasets$Purchased = factor(datasets$Purchased,
#                             levels = c('No','Yes'),
#                             labels = c(0,1))

#Splitting the dataset nto Training set and Test set
library(caTools)
set.seed(123)
split = sample.split(datasets$Purchased, SplitRatio = 0.8)
# #Split Ratio = For Training Set
# training_set = subset(datasets, split == TRUE)
# test_set = subset(datasets, split == FALSE)
# 
# #Feature Scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])
