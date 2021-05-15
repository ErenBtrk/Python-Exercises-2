'''
27. Write a Python program to concatenate all elements in a list into a string and return it.
'''

def function(list):
    new_str = ""
    for item in list:
        new_str += str(item)
    return new_str

my_list = [2,5,1,2131,435,6]
my_list2 = ["hello","world","my","name","is","bat"]

print(function(my_list))
print(function(my_list2))    

