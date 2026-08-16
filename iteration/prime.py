#pallavi Dhuli
#25341A05O3
#prime



num = int(input("Enter a number: "))
is_prime = True

for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is Prime")
else:
    print(num, "is not Prime")
#Enter a number: 12
#12 is not Prime    

