#Natural Language Text
dataset = read.delim('Data/Restaurant_Reviews.tsv', quote = '', stringsAsFactors = FALSE)

#Cleaning the texts
library(tm)