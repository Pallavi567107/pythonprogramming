#name: Pallavi Dhuli
#Case 2: Auto Username Generator 

first_name = input("Enter your first name: ")
roll_no = input("Enter your roll number: ")

username = first_name.lower() + roll_no[-2:]

print("Generated username:", username)
#Enter your first name: pallavi
#Enter your roll number: 25341A05O3
#Generated username: pallaviO3