'''
34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20.

'''

def function(n1,n2):
    if(n1+n2 >= 15 and n1+n2 <= 20):
        return 20
    else:
        return n1+n2

num1 = int(input("Please enter a number : "))
num2 = int(input("Please enter a number : "))

print(function(num1,num2))