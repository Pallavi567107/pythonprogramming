#identity operators
#B7.1
#Name:Pallavi Dhuli

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2) 
print(list1 is list2) 
print(list1 is list3) 
print(id(list1), id(list2), id(list3))

#True
#False
#True
#1661468077952 1661468183168 1661468077952