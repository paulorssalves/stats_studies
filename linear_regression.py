#!/usr/bin/python3


l1 = [5,17,11,8,14,5] # sample list: tips


def mean(list):
    q = len(list)
    s = sum(list)
    return s / q

def return_errors (list): # errors = residuals
    for item in list:
        yield item - mean(list)

def square_errors(list):
    s = []
    for item in list:
        s.append(item*2)
    return s

# the goal of simple linear regression is to create a linear model that
# minimizes the sum of squares of the residuals

# with two variables, we compare the line we have with the data 
# pretending that the independent variable (bill values, in this case)
# doesn't even exist.

# If the data is good, the prediction (SSE (sum of square errors)) will fit the line created by the independent variable

# In a simple linear regression with two variables we compare the best fit regression line (the one with the independent variable)
# to the predicted line, made by the sum of the square 

# The ideal is to minimize the area of the SSE


