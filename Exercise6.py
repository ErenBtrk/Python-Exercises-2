'''
6. Write a Python program which accepts a sequence of comma-separated numbers
 from user and generate a list and a tuple with those numbers.

'''

import re

inputStr = input("Please enter sequence of comma-separated numbers : ").split(',')
myList = list(inputStr)
myTuple = tuple(inputStr)
print(myList)
print(myTuple)