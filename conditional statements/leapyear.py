#Pallavi Dhuli
#25341A05O3
#conditional statement 
#leap year


year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
#Enter a year: 2024
#2024 is a Leap Year    