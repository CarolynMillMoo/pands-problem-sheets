#this program takes the any inputted positive integer and outputs the successive values of the following calculation
#if the integer is even it is divided by two
#if the integer is odd it is multiplied by three and one added
#the program will end if the current value is one
#Author: Carolyn Moorhouse

import sys

def collatz(number):

    if number % 2 == 0:       #conditions for even numbers
        print(number // 2)
        return number //2
    elif number % 2 != 0:     #conditions for odd numbers
        result = 3*number+1
        print(result)
        return result

try:
    number = input('Enter a number:')          #user integer input
    while number != 1:                         #performs a while loop until the number becomes 1
        number = collatz(int(number))          #passes the number to collatz() function until it arrives at 1
except ValueError:
    print('Value Error. Please enter an integer')
