#a program that makes a list of 10 random numbers 20000-80000
#Author: Carolyn Moorhouse

import numpy as np

minSalary = 20000
maxSalary= 80000
numberOfEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print("Salaries:", salaries)

salariesPlus = salaries + 5000
print("Salaries + 5000:", salariesPlus)

salariesMult = salaries * 1.05
print("Salaries Multiplied:", salariesMult)

newSalaries = salariesMult.astype(int)
print("New Salaries:", newSalaries)
