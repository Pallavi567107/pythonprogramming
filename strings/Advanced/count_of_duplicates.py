#25341A05O3
#Pallavi Dhuli

s = input("Enter a string: ")
for ch in set(s):
    if s.count(ch) > 1:
        print(ch, ":", s.count(ch))
#output:
Enter a string: pallavi
a : 2
v : 1
