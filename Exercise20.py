'''
20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

'''
str = input("Please enter a string : ")
while True:
    try:
        n = int(input("How many copies of the string you want : "))
        if(n < 0):
            raise Exception("Please enter a positive number.")
    except Exception as excObject:
        print(excObject)
    else:
        break

new_str = (str+' ') * n
print(new_str)

