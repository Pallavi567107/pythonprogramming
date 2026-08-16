#pallavi Dhuli
#25341A05O3
#sum and avg
num = int(input("Enter a number: "))
temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

average = sum_digits / count 
print("Sum of digits:", sum_digits)
print("Average of digits:", average)

#Enter a number: 12
#Sum of digits: 3
#Average of digits: 1.5