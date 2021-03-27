#this program takes the any inputted positive integer and outputs the successive values of the following calculation
#if the integer is even it is divided by two
#if the integer is odd it is multiplied by three and one added
#the program will end if the current value is one
#Author: Carolyn Moorhouse

import sys

def collatz(number):
    if number % 2 == 0:            #conditions for even number
        result = number // 2
    elif number % 2 == 1:          #conditions for odd number
        result = 3 * number + 1
  
    while result == 1:             #conditions for number 1
        print (result)
        number = result
        return collatz(number)
    while result ! = 1:
        print(result)
        number = result
        return collatz(number)

print('Enter a number')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('You must enter an integer type.')

