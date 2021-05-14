''' 
Write a Python program to get a new string from a given string where "Is" has been added to the front.
 If the given string already begins with "Is" then return the string unchanged. 

'''

inputStr = input("Please enter a string : ").lower()
if(inputStr[0:2] == "is"):
    print(inputStr)
else:
    print("is "+inputStr)