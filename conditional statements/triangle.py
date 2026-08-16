#Pallavi Dhuli
#25341A05O3
#conditional statement 
#triangle

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))


if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")

#Enter side 1: 1
#Enter side 2: 2
#Enter side 3: 2
#Isosceles Triangle    