#Pallavi Dhuli
#25341A05O3
#conditional statement 
#character.py


ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter only one character")
elif ch.isdigit():
    print(ch, "is a Digit")
elif ch in ['A','I','E','O','U','a', 'e', 'i', 'o', 'u']:
    print(ch, "is a Vowel")
elif ch.isalpha():
    print(ch, "is a Consonant")
else:
    print(ch, "is a Special Symbol")

#Enter a single character: a
#a is a Vowel