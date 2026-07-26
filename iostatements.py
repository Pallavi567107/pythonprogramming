#I/O statements ,task :1,Name:Pallavi Dhuli
print("program 1")
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"Hello {name}, you will turn {age + 1} next year.")
print()
#I/O statements ,task :2,Name:Pallavi Dhuli
print("program 2")
print()
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
a = int(n1)
b = int(n2)

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print()
print()
#I/O statements ,task :3,Name:Pallavi Dhuli
name = "Pallavi"; marks = 85
print(name, marks) # comma-separated
print("Name: {} Marks: {}".format(name, marks)) # str.format
print(f"Name: {name} Marks: {marks}") # f-string
print()
print()
#I/O statements ,task :4,Name:Pallavi Dhuli
print()
print()
data = input("Enter numbers separated by space: ") 
nums = [int(x) for x in data.split()]
print("Sum:", sum(nums))

# CHALLENGE: Average of 3 subjects
marks = input("Enter 3 subject marks: ")
m = [int(x) for x in marks.split()]
avg = sum(m) / 3
print(f"Average: {avg:.2f}")
