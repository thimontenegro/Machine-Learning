#Simple Linear Regression

dataset = read.csv('Salary_Data.csv')

#Splitting the dataset into the training set and test set
#install.packages('caTools')
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


#Fitting Simple Linear regression to the Training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set )
#Salary is propotional to years of experience


#Predicting the Test set Results
predict_values = predict(regressor, newdata = test_set)


#Visualising the Training set Results
# install.packages('ggplot2')
library(ggplot2)

ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') +
  geom_line(aes( x= training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
           colour = 'black') + 
  ggtitle('Salary vs Experience (Training set)') +
  xlab('Years of Experience') +
  ylab('Salary')


ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
                colour = 'black') +
  ggtitle('Salary vs Experience (Test Set)') +
  xlab('Years of experience') +
  ylab('Salary')
  