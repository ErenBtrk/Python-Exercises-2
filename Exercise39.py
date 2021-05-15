'''
39. Write a Python program to compute the future value of a specified principal amount,
 rate of interest, and a number of years.
 
 '''

def function(value,rate,years):
    return value*(1+rate*0.01)**years


future = function(10000,3.5,7)
print(f"{future:.2f}")