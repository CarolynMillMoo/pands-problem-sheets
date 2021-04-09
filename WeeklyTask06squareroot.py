#A program that takes a positive floating-point number input
#and outputs an approximation of its square root
#Author: Carolyn Moorhouse

def newton_method(number, number_iters = 500):
    a = float(number) #this is the number the program will get the square root of
    for i in range(number_iters):
       number = 0.5 * (number + a / number)
    #x_(n+1) = 0.5*(x_n +a / x_n)
    return number
number = float(input("Please enter a positive number:"))
sqrtNumber = newton_method(number)

print ('The square root of {} is approx {}'.format(number, sqrtNumber))