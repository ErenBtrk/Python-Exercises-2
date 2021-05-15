'''
32. Write a Python program to get the least common multiple (LCM) of two positive integers.

'''

def function(n1,n2):
    lcm = 1
    i = 2
    while(n1 != 1 or n2 != 1):
        if(n1 % i == 0 and n2 % i == 0):
            n1 = n1/i
            n2 = n2/i
            lcm *= i
        elif(n1 % i == 0):
            n1 = n1/i
            lcm *= i
        elif(n2 % i == 0):
            n2 = n2/i
            lcm *= i
        else:
            i += 1
    return lcm
    


number1 = int(input("Please enter a number : "))
number2 = int(input("Please enter a number : "))

print(function(number1,number2))


##############################################################################

def function2(n,m):
    n1=n
    m1=m
    while( m1 != n1 ):
        if( m1 > n1 ):
            n1 += n
        else:
            m1 += m
    return m1

n = int(input("Please enter a number : "))
m = int(input("Please enter a number : "))

print(function2(n,m))



