#SVR
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#fitting the SVR to the dataset
library(e1071)
regressor = svm(formula = Salary ~ .,
                data = dataset,
                type = 'eps-regression')
#most important argument = Type

#Predict a new result
y_pred = predict(regressor, data.frame(Level = 6.5))

#Visualising the SVR resultts
library(ggplot2)
ggplot() + 
    geom_point(aes(x = dataset$Level, y = dataset$Salary),
               colour = 'red') +
    geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
              colour = 'blue')  +
    ggtitle('Truth or Bluff (SVR)') +
    xlab('Level') + 
    ylab('Salary')