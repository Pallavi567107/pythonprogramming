#25341A05O3
#Pallavi Dhuli
s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word:", longest)
#output:
Enter a sentence: my name is pallavi
Longest word: pallavi
