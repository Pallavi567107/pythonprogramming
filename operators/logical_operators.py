#logical operators
#B4.1
#Name:Pallavi Dhuli


percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))
eligible = percentage > 75 and attendance > 90
print("Eligible for scholarship:", eligible)

#Enter percentage: 86
#Enter attendance %: 92
#Eligible for scholarship: True