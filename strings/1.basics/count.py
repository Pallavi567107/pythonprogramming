#Name:Pallavi Dhuli
#Jntu no: 25341A05O3
s = input("Enter string: ")

v = c = d = sp = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        v+=1
    elif ch.isalpha(): # alphabet but not vowel = consonant
        c+=1
    elif ch.isdigit():
        d+=1
    elif ch.isspace():
        sp+=1

print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Spaces: {sp}")
#Enter string: write once run anywhere
#Vowels: 8, Consonants: 12, Digits: 0, Spaces: 3




       