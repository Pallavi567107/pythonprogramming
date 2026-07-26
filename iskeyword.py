#keywords ,task no:2,Name:Pallavi Dhuli  
import keyword
key_word=input("enter a word to check if it is keyword or not")
result=keyword.iskeyword(key_word)
print(key_word+" is keyword in python:[true|false]"+str(result))


print()
print("program 2")
print()
#keywords ,task no:1,Name:Pallavi Dhuli
import keyword
l=len(keyword.kwlist)
print(l)
for keywords in keyword.kwlist:
   print(keywords)
#challenge (keywords)   
print("soft kerwords are")   
for keywords in keyword.softkwlist:
   print(keywords)   



print()
print("program 3")
print()
#keyword ,tast no:3,Name:Pallavi Dhuli
for=5
True=10
print(for)
print(True)
#    for=5
#     ^
#SyntaxError: invalid syntax