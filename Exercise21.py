'''
21. Write a Python program to find whether a given number (accept from the user) is even or odd,
 print out an appropriate message to the user. 
'''

number = int(input("Please enter a number : "))

if(number % 2 == 0):
    print(f"The number({number}) you have entered is an EVEN number")
else:
    print(f"The number({number}) you have entered is an ODD number")