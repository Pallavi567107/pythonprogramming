#pallavi Dhuli
#25341A05O3
#count


s = input("Enter a string: ")
vowels = consonants = digits = spaces = 0

for ch in s:
    if ch.lower() in ['a','e','i','o','u']:
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
#Enter a string: hi 33
#Vowels: 1
#Consonants: 1
#Digits: 2
#Spaces: 1