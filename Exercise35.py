'''
35. Write a Python program that will return true if the two given integer values
 are equal or their sum or difference is 5.
 
 '''

def function(n1,n2):
    sum = n1+n2
    diff = abs(n1-n2)
    if(n1 == n2 or sum == 5 or diff == 5):
        return True
    else:
        return False

number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))

print(function(number1,number2))