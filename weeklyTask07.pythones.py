#This Program will read in text file "weeklyTask07Ch1HP&PSSummary.txt"
#and will output the number of e's it contains
#Author: Carolyn Moorhouse
 
filename = "weeklyTask07.Ch1HP&PS.txt"

with open(filename, "r", encoding="latin-1") as f:
    data = f.read()
    occurences = data.count("e")

print('Number of occurences of e:', occurences)