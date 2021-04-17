
file = "weeklyTask07.Ch1HP&PS.txt"

def letterCount(file, letter):
   with open(file, 'r') as f:
       text = f.read()
       return text.count('e')


print(letterCount(file, 'e'))
