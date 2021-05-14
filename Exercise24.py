'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''

vowel_list = "aeiou"

while True:
    try:
        letter = input("Please enter a letter : ")
        if(not letter.isalpha()):
            raise Exception("You have not entered a letter.")
        if(len(letter) != 1):
            raise Exception("Invalid length.")
    except Exception as excObject:
        print(excObject)
    else:
        break

if(letter in vowel_list):
    print(f"The letter({letter}) you have entered is a vowel")
else:
    print(f"The letter({letter}) you have entered is NOT a vowel")