##################################################
## load required packages ########################
##################################################

import pandas as pd
import numpy as np

##################################################
## read in data ##################################
##################################################

data = pd.read_csv('01-input.txt',
                   sep = "   ",
                   header = None,
                   engine = 'python')

##################################################
## process data ##################################
##################################################

## pull out sorted first column
A = data[0].sort_values().reset_index(drop = True)

## pull out sorted second column
B = data[1].sort_values().reset_index(drop = True)

## smoosh them back together
updated_data = pd.concat([A, B], axis = 1)
updated_data.columns = ["A", "B"]

## calculate distance
updated_data["distance"] = abs(updated_data["A"] - updated_data["B"])

##################################################
## solution: part A ##############################
##################################################

#print(sum(updated_data["distance"]))

##################################################
## solution: part B ##############################
##################################################

## move over to numpy
a = A.values
b = B.values

## use the histogram function to calculate counts per item
a_counts = np.bincount(a)
b_counts = np.bincount(b)

print(sum(a_counts[:len(b_counts)]*b_counts*np.arange(len(b_counts))))