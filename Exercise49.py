'''
49. Write a Python program to list all files in a directory in Python.
'''

from os import PathLike, listdir
from os.path import isfile, join

new_list = listdir(r"C:\Users\erenb\Desktop\Programlar")

for item in new_list:
    print(item)
