from matplotlib import pyplot as plt
from math import sqrt

l1 = [5,17,11,8,14,5] # sample list: tips
l2 = [34, 108, 64, 88, 99, 51] # bills

def mean(list):
    q = len(list)
    s = sum(list)
    return s / q

# the goal of simple linear regression is to create a linear model that
# minimizes the sum of squares of the residuals

# with two variables, we compare the line we have with the data 
# pretending that the independent variable (bill values, in this case)
# doesn't even exist.

# If the data is good, the prediction (SSE (sum of square errors)) will fit the line created by the independent variable

# In a simple linear regression with two variables we compare the best fit regression line (the one with the independent variable)
# to the predicted line, made by the sum of the square 

# The ideal is to minimize the area of the SSE

def line(m, x, b):
    y = m*x + b # m = slope of the line (rise/run)
    # b = y-intercept | y-intercept=2-tuple in which x value is always zero
    return y

# Beta0 = b (y-intercept)
# Beta1 = m (slope)
# Epsilon = error term

# Simple linear regression equation:
# E(y) = Beta0 + Beta1*x # expected value of y equals...
# Y is not a point, but a mean of distribution

# in case of sample data: ŷ = b0 + b1*x

def slope(x, y):
    # list of every item in x minus the mean of x 
    l_x = [i - mean(x) for i in x] 

    # list of every item in y minus the mean of y 
    l_y = [i - mean(y) for i in y]

    l_product = [i * j for i, j in zip(l_x, l_y)]
    return sum(l_product)/sum([x**2 for x in l_x])

# it could be simplified by simply typing this out:
# return sum([i*j for i,j in zip(return_errors(x), return_errors(y))]/sum([x**2 for x in return_errors(x)])

def intercept(x, y):
    ybar = mean(y) # bar implies 'mean of'
    xbar = mean(x)
    return ybar - (slope(x, y) * xbar)

def estimate_coefficients(x, y):
    return (intercept(x, y),slope(x,y))

# being the regression line such as:
# yhat = beta0 + beta1 * xi
# being beta0 the intercept of x,y
# and beta1 the slope of x,y

def get_regression_line(x, y, coefficient):
    l = []
    for i in x:
        l.append(coefficient[0] + coefficient[1] * i)
    """    
    # same thing as: 
    for i in x:
        l.append(intercept(x,y) + slope(x,y)*i) 
    """
    return l
        
def return_errors (list): # errors = residuals
    for item in list:
        yield item - mean(list)

def square_errors(list):
    s = []
    for item in list:
        s.append(item**2)
    return s

# the SST is the sum of the squares difference between
# dependent variable and the mean

# SSR is the sum of the square difference
# between the regression-predicted
# value and the mean (sum of squares due to regression)

# SSE is the sum of the square difference
# between the values of the
# dependente variable and the predicted value

def SST(list): # sum of squares total
    # sum of the differences between the
    # dependent variable and its mean
    errors = return_errors(list)
    return sum(square_errors(errors))

def SSR(regline_l, var_l):
    # get the SSR out of the differences between
    # the values predicted by the regression and
    # the mean of var_l
    l = []
    for i in regline_l:
        l.append(i - mean(var_l))
    return sum([x**2 for x in l])

def SSE(depvar_l, regline_l):
    # sum of square errors, comparing
    # the dependent variable to the
    # regression line 
    l = []
    for i,j in zip(depvar_l, regline_l):
        l.append(i-j)
    return sum([x**2 for x in l])

def determination_coefficient(SSR, SST):
    return SSR/SST

# for data to be good, we want the SSE to be as low as possible
