'''
26. Write a Python program to create a histogram from a given list of integers.

'''

import random

my_list = [random.randrange(1,50) for i in range(50)]

print(my_list)

frequency_list = [0 for item in range(50)]

print(frequency_list)

for index in range(len(my_list)):
    frequency_list[my_list[index]] += 1

for index in range(len(frequency_list)):
    print(index,':','*'*frequency_list[index])
    