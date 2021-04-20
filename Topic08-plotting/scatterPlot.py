#a program that makes a list of ages and has the same salary
#info as topic08 question01 and makes a scatter plot of the data
#Author: Carolyn Moorhouse

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 21, high = 65, size = numberOfEntries)

plt.scatter(ages, salaries, label = "salaries")
#plt.show()

#xpoints = np.array(range(1, 101))
#ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints, color = 'r', label = "x squared")

plt.title("Random Plot")
plt.xlabel("Age")
plt.ylabel("Salaries")
plt.legend()
#plt.show()

#plt.savefig('prettier-plot.png')

