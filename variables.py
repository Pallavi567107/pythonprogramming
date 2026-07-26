#variables ,task :1,Name:Pallavi Dhuli
name="pallavi"
height=5.9
age=19
is_student=True
print(name+" type:", type(name))
print(str(height)+" type:",type(height))
print(str(age)+" type:",type(age))
print(str(is_student)+" type:",type(is_student))

#variables ,task :2,Name:Pallavi Dhuli
a,b,c=10,20,30
a=b=c=100
print("a=",a,"b=",b,"c=",c)

#variables ,task :3,Name:Pallavi Dhuli
#3a using third variable(swap)
a=10
b=20
print("before swaping a=",a,"b=",b)
temp=a
a=b
b=temp
print("after swaping swaping a=",a,"b=",b)

#3b using python tuple-unpacking
a=10
b=20
print("before swaping a=",a,"b=",b)
a,b=b,a
print("after swaping a=",a,"b=",b)


#variables ,task :4,Name:Pallavi Dhuli
number = 20
print(number,"type:",type(number))
number="name"
print(number,"type:",type(number))

#challenge(variables)
radius=float(input("radius:"))
PI=3.14
area=PI*radius*radius
circumference=2*PI*radius
print("area :",area)
print("circumference:",circumference)