#I/O statements 
# task :4,
# Name:Pallavi Dhuli
data = input("Enter numbers separated by space: ") 
nums = [int(x) for x in data.split()]
print("Sum:", sum(nums))
#Enter numbers separated by space: 10 20 11
#Sum: 41
