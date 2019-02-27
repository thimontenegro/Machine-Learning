datasets$Country = factor(datasets$Country,
                          levels = c('France','Spain','Germany'),
                          labels = c(1,2,3))

datasets$Purchased = factor(datasets$Purchased,
                            levels = c('No','Yes'),
                            labels = c(0,1))