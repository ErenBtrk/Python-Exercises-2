'''
Write a Python program to get the n (non-negative integer) copies of the first 2
characters of a given string. Return the n copies of the whole string if the length is less than 2
 
'''

while True:
    try:
        n = int(input("Please enter how many copies you want : "))
        if(n < 0):
            raise Exception("Please enter a poisitive number.")
    except Exception as excObject:
        print(excObject)
    else:
        break

my_str = input("Please enter a string : ")
while True:
    try:
        howManyChars = int(input("How many characters of the string do you want to copy : "))
        if(howManyChars > len(my_str) or howManyChars < 0):
            raise Exception("Invalid number of chars.")
    except Exception as excObject:
        print(excObject)
    else:
        break
        
new_str = (my_str[0:howManyChars]+' ') * n

print(new_str)