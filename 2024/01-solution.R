##################################################
## load required libraries #######################
##################################################

library(readr) ## for reading in csvs
library(dplyr) ## for data manipulation

##################################################
## read in data ##################################
##################################################

data <- read_delim("01-input.txt",
                   delim = "   ",
                   col_names = c("A", "B"),
                   show_col_types = FALSE)

##################################################
## process data ##################################
##################################################

## pull out sorted first column
A <- sort(data$A, decreasing = FALSE)

## pull out sorted second column
B <- sort(data$B, decreasing = FALSE)

## smoosh them back together
updated_data <- cbind.data.frame(A, B)

## calculate distance
updated_data$distance <- abs(updated_data$A - updated_data$B)

##################################################
## solution: part A ##############################
##################################################

sum(updated_data$distance)

##################################################
## solution: part B ##############################
##################################################

## count the number of times each element of B occurs, just look at 
## items that also occur in A
count_table <- table(B)[as.character(A)]

## calculate the weird similarity score
sum(as.numeric(count_table)*as.numeric(names(count_table)), na.rm = TRUE)
