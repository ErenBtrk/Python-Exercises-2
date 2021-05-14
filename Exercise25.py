'''
25. Write a Python program to check whether a specified value is contained in a group of values.
'''
import random

number_list = [random.randrange(50) for i in range(10) ]

number = int(input("Please enter a number : "))

print(number_list)

if(number in number_list):
    print(f"The number({number}) you have entered is in the list .")
else:
    print(f"The number({number}) you have entered is NOT in the list.")