'''
Write a Python program to count the number 4 in a given list. 
'''

my_list = [1, 4, 6, 4, 7, 4,4]

count = 0
for item in my_list:
    if(item == 4):
        count += 1

print(f"The count of the number(4) in the list is : {count}")