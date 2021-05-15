'''
31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
'''

def function(n1,n2):
    while n1 != n2:
        if n1 > n2:
            n1 = n1-n2
        else:
            n2 = n2-n1
    return n1

number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))

print(function(number1,number2))