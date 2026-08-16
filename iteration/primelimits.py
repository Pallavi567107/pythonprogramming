#pallavi Dhuli
#25341A05O3
#primenumbers



start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers between", start, "and", end, "are:")
for n in range(start, end + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n,end=" ")   

#Enter starting number: 2
#Enter ending number: 4
#Prime numbers between 2 and 4 are:
#2 3             