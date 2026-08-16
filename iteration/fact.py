#pallavi Dhuli
#25341A05O3
#factorial

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)

#Enter a number: 3
#Factorial of 3 is 6