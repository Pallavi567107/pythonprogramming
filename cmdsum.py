#command line arguments task 2 ,name:pallavi 
import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
print("Sum:", a + b)
#task 3
print("Script name:", sys.argv[0])
print("Total args:", len(sys.argv) - 1)
