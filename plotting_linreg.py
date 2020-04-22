from linear_regression import *
from matplotlib import pyplot as plt
from correlation import correlation as r 

x_axis = list(range(20, 140, 20))
y_axis = list(range(4, 24, 4))

plt.xticks(x_axis)
plt.yticks(y_axis)

b = estimate_coefficients(l2, l1)
r_line = get_regression_line(l2, l1,b)

pearsonr = r(l2, l1)

plt.title("Relationship between tip and bill values")
plt.xlabel("Bill value")
plt.ylabel("Tip value")
plt.plot(l2, l1, 'ro', label="tip values")
plt.plot(l2, r_line, color="g", label="regression line")

centroid_x= [mean(l2)]
centroid_y = [mean(l1)]

plt.plot(centroid_x, centroid_y, 'ko', label="centroid")
plt.text(60, 16, 'r={}'.format(pearsonr))
plt.grid()
plt.legend()
plt.show()
    
