#A program that plots the funtion y = x^2
#Author: Carolyn Moorhouse

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,100))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()