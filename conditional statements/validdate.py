#Pallavi Dhuli
#25341A05O3
#conditional statement 
#valid  date



year = int(input("Enter year: "))
month = int(input("Enter month 1-12: "))
day = int(input("Enter day: "))


is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


if month in [1, 3, 5, 7, 8, 10, 12]:
    max_days = 31
elif month in [4, 6, 9, 11]:
    max_days = 30
elif month == 2:
     if is_leap:
       max_days = 29
     else :
         max_days=28
else:
    max_days = 0


if month < 1 or month > 12:
    print("Invalid Date: Month should be 1-12")
elif day < 1 or day > max_days:
    print("Invalid Date")
else:
    print("Valid Date:", day, "/", month, "/", year)

#Enter year: 2024
#Enter month 1-12: 2
#Enter day: 29
#Valid Date: 29 / 2 / 2024    