#This Program will read in text file "weeklyTask07Ch1HP&PSSummary.txt"
#and will output the number of e's it contains
#Author: Carolyn Moorhouse
 
filename = "weeklyTask07.Ch1HP&PS.txt"

with open(filename, "r") as f:
    text = f.read(25)
    print(text)
    