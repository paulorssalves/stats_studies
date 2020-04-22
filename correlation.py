from standard_deviation import std_deviation
from linear_regression  import mean
from math import sqrt

# 2012 data
SP500 = [0.039787, 0.030852, -0.00753, -0.0647, 0.038793, 0.012519, 0.019571, 0.023947, -0.01999, 0.002843, 0.007043, 0.030718]

DJI = [0.02495, 0.01987, 0.00012, -0.06408, 0.03851, 0.00993, 0.00630, 0.02611, -0.02568, -0.00543, 0.00601, 0.02030] 

workers = [12,30,15,24,14,18,28,26,19,27]
tables = [20,60,27,50,21,30,61,54,32,57]
 
# cov(x,y) = sum((xi-xline)(yi-yline))/n-1
def covariance(x, y):
    # list of every item in x minus the mean of x 
    l_x = [i - mean(x) for i in x] 

    # list of every item in y minus the mean of y 
    l_y = [j - mean(y) for j in y]

    # list of the product of every item to its corresponding value in the two previously created lists
    m_b = [i * j for i,j in zip(l_x, l_y)]
    return sum(m_b)/(len(x)-1)

def correlation(x, y):
    c = covariance(x, y)
    r = c / (std_deviation(x) * std_deviation(y))
    return r

# if |r| >= 2/sqrt(n) then a relationship exists
def verify_correlation(r, n):
    # r = correlation coefficient
    # n = sample size
    if abs(r) >= 2/sqrt(n):
        return True, "|r|={}, 2/sqrt(n)={}".format(abs(r), 2/sqrt(n))
    else:
        return False, "|r|={}, 2/sqrt(n)={}".format(abs(r), 2/sqrt(n))

