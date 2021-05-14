'''
Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference
'''

import math

number = int(input("Please enter a number : "))
diff = number - 17

if(number > 17):
    print(f"{diff*2}")
if(number < 17):
    print(f"{abs(diff)}")