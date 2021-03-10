#this program takes a persons height and weight and calculates their BMI
#Author: Carolyn Moorhouse
#this programme also converts cm squared to metres squared


height = float(input ("Please enter your height in cm: "))
weight = float(input ('Please enter your weight in kg:'))

bmi = weight/((height*height)/10000)

print('This is your BMI:' + format(bmi, '.2f'))

