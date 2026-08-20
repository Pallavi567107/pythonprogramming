#Pallavi Dhuli
#25341A05O3
#inverted centered triangle

n=int(input("enter n: "))
for i in range(1,n+1):
    print(" "*i,end=" ")
    for j in range(n-i+1,0,-1):
        print("*",end=" ")
    print()    

#enter n: 5
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 

