from math import sqrt

def mean(list):
    q = len(list)
    s = sum(list)
    return s / q

def variance(list, is_sample=True):
    m = mean(list)
    l = []
    for i in list:
        l.append((i-m)**2)
    if is_sample == True:
        return sum(l)/(len(l)-1) 
    else: #if not sample, but population (a correction) 
        return sum(l)/len(l)

# standard_deviation(L) = sqrt(variance(L))

def std_deviation(l, is_sample=True):
    if is_sample == True:
        return sqrt(variance(l))
    else:
        return sqrt(variance(l, is_sample=False))

