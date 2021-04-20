#this program is to make a pie plot of the unique occurences of values in an array
#Author: Carolyn Moorhouse

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Wexford', 'Cork', 'Kerry', 'Galway', 'Clare']

counties = np.random.choice(
    possibleCounties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels = unique)

#plt.show()

plt.bar(unique, counts)
plt.show()

