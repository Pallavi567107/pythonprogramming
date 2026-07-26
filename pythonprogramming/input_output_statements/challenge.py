
# CHALLENGE: Average of 3 subjects
marks = input("Enter 3 subject marks: ")
m = [int(x) for x in marks.split()]
avg = sum(m) / 3
print(f"Average: {avg:.2f}")
