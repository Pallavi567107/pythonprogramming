#indentation ,task :1,Name:Pallavi Dhuli
x = 5
if x > 0:
    print("Positive")
print()
#indentation ,task :2,Name:Pallavi Dhuli
print("program-2")
print()
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

print()
print("program-3")
#indentation ,task :3,Name:Pallavi Dhuli
print()
x = int(input("Enter x: "))
if x > 0:
    print("positive")
else:
    print("non-positive")

# CHALLENGE: 3 level nested - star triangle
for i in range(1, 5): # level 1
    for j in range(i): # level 2
        if j < i: # level 3
            print("*",end=" ")
    print()