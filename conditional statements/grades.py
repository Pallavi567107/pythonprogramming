#Pallavi Dhuli
#25341A05O3
#conditional statement 
#grades

marks = float(input("Enter student's marks out of 100: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks")

#Enter student's marks out of 100: 23
#Grade: F
