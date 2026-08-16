#Pallavi Dhuli
#25341A05O3
#conditional statement 
#largest


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print("The largest number is:", largest)

#Enter first number: 12
#Enter second number: 12
#Enter third number: 13
#The largest number is: 13.0