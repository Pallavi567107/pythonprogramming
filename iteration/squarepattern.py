#pallavi dhuli
#25341a05o3
#square pattern


num=int(input("enter rows: "))
for n in range(1,num+1):
    for m in range(1,num+1):
        if n==1 or n==num or m==1 or m==num:
           print("*",end=" ")
        else:
            print(" ",end=" ")   
      
    print()   

#enter rows: 4
#* * * * 
#*     * 
#*     * 
#* * * *      