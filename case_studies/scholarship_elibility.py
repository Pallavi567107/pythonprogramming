#name: Pallavi Dhuli
#Case 8: Scholarship Eligibility Check 

percentage=float(input("enter precentage"))
income=int(input("enter family income"))
if (percentage>85) or ((percentage>75) and (income<200000)):
    print("eligible")
else:
    print("not eligible")
#enter precentage50
#enter family income20000
#not eligible