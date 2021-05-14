'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
'''

total = 0

while True:
    try:
        userInput = int(input("Please enter a number : "))
        if(userInput < -9 or userInput > 9):
            raise Exception("Please enter a number between 0-9.")
    except Exception as excObject:
        print(excObject)
    else:
        break
    
number = userInput

for index in range(3):
    total += number
    number = number *10 + userInput
    
print(total)


##########################################################################################################

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)