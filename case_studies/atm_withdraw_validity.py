#name: Pallavi Dhuli
#Case 3: ATM Cash Withdrawal 
balance=int(input("enter balance amount: "))
withdraw=int(input("enter amount to withdraw: "))
if balance<withdraw:
    print("invalid")
else:
    print("valid")

#enter balance amount: 10000
#enter amount to withdraw: 4500
#valid