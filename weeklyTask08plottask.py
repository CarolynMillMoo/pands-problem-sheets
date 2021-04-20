#a program which displays a plot of the functions:
#f(x) = x, g(x) = x^2, and h(x)=x^3 in the range [0,4]
#Author: Carolyn Moorhouse

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(0, 4))
fxpoints = xpoints
gxpoints = xpoints * xpoints
hxpoints = gxpoints * xpoints

plt.plot(xpoints, fxpoints, label = 'f(x) = x')
plt.plot(xpoints, gxpoints, label = 'g(x) = x^2')
plt.plot(xpoints, hxpoints, label = 'h(x) = x^3')
plt.title("Plot Task", color = 'b')
plt.xlabel("X", color ='r')
plt.ylabel("Functions of X", color = 'g')
plt.legend()  

plt.show()