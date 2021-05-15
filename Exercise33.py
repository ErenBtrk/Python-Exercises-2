'''
33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

'''

my_list = []
isEqual = False
sum = 0
i = 0

while i < 3:
    number = int(input("Please enter a number : "))
    sum += number
    if(number in my_list):
        isEqual = True
    my_list.append(number)
    i += 1

if(isEqual):
    sum = 0

print(sum)







    





    