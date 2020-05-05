from matplotlib import pyplot as plt
from standard_deviation import std_deviation
from math import sqrt

l1 = [5,17,11,8,14,5] # sample list: tips
l2 = [34, 108, 64, 88, 99, 51] # bills

t = 2.776 # t distribution with 4 levels of freedom (6 - 2), in that 6 is the number of the samples

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

b = estimate_coefficients(l2, l1)

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

rl = get_regression_line(l2, l1, b)
        
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

def SSR(regline_l, var_l): # sum of squares difference
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

def MSE(depvar_l, regline_l):
    # mean square error
    return SSE(depvar_l, regline_l)/(len(depvar_l) - 2)

def standard_error(depvar_l, regline_l):
    # how spread out the data points are from the regression line
    # lower is better
    return sqrt(MSE(depvar_l, regline_l))

def determination_coefficient(SSR, SST):
    return SSR/SST

# for data to be good, we want the SSE to be as low as possible


def standardize(var_l):

    var_mean = mean(var_l)
    var_dev = std_deviation(var_l, is_sample=False)
    return [(var - var_mean)/var_dev for var in var_l]

# original regression slope = correlation * (std(y)/std(x))
# thus:
# correlation = original regression slope * (std(x)/std(y))

# using standardized variables can be useful
# 
# when we have variables in very different scales and variances

def rsquared(depvar_l, regline_l):
    return SSR(regline_l, depvar_l)/SST(depvar_l)

# confidence interval for the slope:

# b1 +/- ta/2^Sb1
# READ: b sub 1 + or - t sub alpha/2^S sub 1
# such that:

# b1 = point estimator for the slope
# t_sub_a/2^S_sub1 = margin of error
# t sub a/2 = t value
# S sub 1 = standard deviation of the slope

def root_mean_square_error(depvar_l, regline_l):
    return sqrt(MSE(depvar_l, regline_l))

def slope_std_deviation(depvar_l, indepvar_l, regline_l):
    sigma_x = sum(square_errors(return_errors(indepvar_l)))
    RMSE = root_mean_square_error(depvar_l, regline_l)
    return RMSE/sqrt(sigma_x)

slope_std_dev = slope_std_deviation(l1, l2, rl)

def t_statistic(std_dev_slope, slope_estimate, t_value):
    r = slope_estimate/std_dev_slope
    if r > t_value:
        return r, "SIGNIFICANT"
    else:
        return r, "NOT SIGNIFICANT"

def slope_conf_interval(slope_estimate, t_value, slope_std_deviation):
    mult = t_value * slope_std_deviation
    r = slope_estimate - mult, slope_estimate + mult
    if 0 in r:
        return r, "NULL HYPOTHESIS TRUE"
    else:
        return r, "REJECT THE NULL"

