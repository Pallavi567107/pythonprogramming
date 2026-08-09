#name: Pallavi Dhuli
#Case 4: Employee Salary and Bonus 

salary = int(input("Enter the base salary: "))

for year in range(1, 4):
    salary += salary * 0.10
    print("Salary after year", year, ":", salary)
#Enter the base salary: 10000
#Salary after year 1 : 11000.0
#Salary after year 2 : 12100.0
#Salary after year 3 : 13310.0    