'''
45.Write a python program to call an external command in Python.

'''

import subprocess

list_files = subprocess.run(["ls", "-l"],shell=True)
print("Hello world")
print("The exit code was: %d" % list_files.returncode)

