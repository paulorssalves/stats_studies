#!/usr/bin/env python
# coding: utf-8

# In[79]:


import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.api import OLS
from matplotlib import pyplot as plt
import seaborn as sn # for heat map
import pandas as pd


# In[128]:


# ideally, a independent variables should not 
# be correlated among themselves
# we're going to use the estimated multiple
# regression equation

# ŷ = b0 + b1x1 + b2x2 + ... bpxp

# BLUE lines are for correlation comparisons 
# between indepedendent variables

# RED are between DEPENDENT and INDEPENDENT


# In[4]:


miles_traveled = np.asarray([89, 66, 78, 111, 44, 77, 80, 66, 109, 76])
num_deliveries = np.asarray([4, 1, 3, 6, 1, 3, 3, 2, 5, 3])
gas_price = np.asarray([3.84, 3.19, 3.78, 3.89, 3.57, 3.57, 3.03, 
            3.51, 3.45, 3.25])
travel_time = np.asarray([7, 5.4, 6.6, 7.4, 4.8, 6.4, 7,
                  5.6, 7.3, 6.4])


# In[110]:


data = {
    "Miles travelled": miles_traveled,
    "Number of deliveries": num_deliveries,
    "Gas price": gas_price,
    "Travel time in hours": travel_time
}
df = pd.DataFrame(data, columns=["Miles travelled", 
                                 "Number of deliveries",
                                "Gas price",
                                "Travel time in hours"])


# In[57]:


def plot_regression_line(independent_variable, dependent_variable, color):
    slope, intercept, r_value, p_value, std_err = stats.linregress(independent_variable, dependent_variable)
    
    # independent variable goes on the x axis
    plt.plot(independent_variable, dependent_variable, 'o', label="original",)
    plt.plot(independent_variable, intercept + slope * independent_variable, color, label="fitted")
    plt.legend()
    plt.show()
    print("slope:\t\t{}\nintercept:\t{}\nr:\t\t{}\np:\t\t{}\nstd_err:\t{}".format(slope, intercept, r_value, p_value, std_err))
    print("R squared:\t{}".format(r_value**2))


# In[92]:


plot_regression_line(miles_traveled, travel_time, 'r')


# In[93]:


plot_regression_line(num_deliveries, travel_time, 'r')


# In[85]:


# apparently gas price no relationship 
# with our dependet variable
# thence, we will not use it for the
# regression analysis
plt.scatter(gas_price, travel_time)


# In[103]:


# now we're going to compare the correlation 
# between independent variables
plot_regression_line(miles_traveled, num_deliveries, 'b')
stats.pearsonr(miles_traveled, num_deliveries)


# In[102]:


plt.scatter(miles_traveled, gas_price)
stats.pearsonr(miles_traveled,gas_price)
# no correlation here


# In[100]:


plt.scatter(num_deliveries, gas_price)
# no correlation here


# In[105]:


stats.pearsonr(num_deliveries, gas_price)


# In[106]:


# using highly correlated independent variables in
# multiple regression would be *REDUNDANT*
# therefore we should remove one of them


# In[111]:


print(df)


# In[112]:


corrMatrix = df.corr()


# In[117]:


print(corrMatrix)


# In[116]:


sn.heatmap(corrMatrix, annot=True)
plt.show()


# In[16]:


# correlations of travel time in hours with other variables

print("p-value (corr. with miles traveled):")
stats.pearsonr(travel_time, miles_traveled)[1]


# In[11]:


print("p-value (corr. with num. deliveries):")
stats.pearsonr(num_deliveries, travel_time)[1]


# In[15]:


print("p-value (correlation with gas price):")
stats.pearsonr(gas_price, travel_time)[1]


# In[59]:


slope, intercept, r, p, stderr = stats.linregress(miles_traveled, travel_time)


# In[60]:


stderr


# In[62]:


plot_regression_line(miles_traveled, travel_time, 'r')


# In[88]:


b = OLS(miles_traveled, travel_time).fit()


# In[89]:


b.summary()


# In[ ]:




