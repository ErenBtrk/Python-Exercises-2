'''
36. Write a Python program to add two objects if both objects are an integer type.

'''

number1 = 5
number2 = 10
number3 = 5.2

if(type(number1) == type(number2) == int):
    print(number1+number2)

if(type(number2) == type(number3) == int):
    print(number2+number3)

####################################################################################################

def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

print(add_numbers(10, 12))

