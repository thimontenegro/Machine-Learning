#Random Forest Regression
dataset = read.csv('Data/Position_Salaries.csv')
dataset = dataset[2:3]

#Fitting Random Florest Regression to the dataset
#install.packages('randomForest)
library(randomForest)
set.seed(seed = 1234)
regressor = randomForest(x = dataset[1],#da o dataframe, variavel independente
                         y = dataset$Salary,
                         ntree = 500)#Faz um vetor dos salarios
#Predicting a new result
y_pred = predict(regressor, data.frame(Level = 6.5))
#Visualising the Random Forest Regression result
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
    geom_point(aes(x = dataset$Level, y = dataset$Salary), colour = 'red') +
    geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))), colour = 'blue') +
    ggtitle('Truth or Bluff (Random Forest Regression)') +
    xlab('Level') +
    ylab('Salary')
