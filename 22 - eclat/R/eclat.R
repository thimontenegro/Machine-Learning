#Eclat
#install.packages('arules')
library(arules)
dataset = read.csv('Data/Market_Basket_Optimisation.csv', header = FALSE)
dataset = read.transactions('Data/Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset, topN = 10)

#Training Apriori on the dataset
rules = eclat(data = dataset,
                parameter = list(support =0.003 , minlen= 2 ))


#Visualising the results
inspect(sort(rules,by = 'support')[1:10])