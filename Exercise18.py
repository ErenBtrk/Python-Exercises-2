'''
Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum. 
'''
i = 0
sum = 0
isEqual = True

while i < 3:
    number = int(input("Please enter a number :"))
    if(i == 0):
        temp = number    
    sum += number
    i += 1
    if(temp != number):
        isEqual = False

if(isEqual):
    print(f"{sum*3}")
else:
    print(f"{sum}")

    

# def sum_thrice(x, y, z):

#      sum = x + y + z
  
#      if x == y == z:
#       sum = sum * 3
#      return sum

# print(sum_thrice(1, 2, 3))
# print(sum_thrice(3, 3, 3))
    
