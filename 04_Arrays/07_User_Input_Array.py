from array import *

arr=array("i",[])
size=int(input("Enter the Size of the Array : "))

for i in range(0,size):
    key=int(input("Enter the Element : "))
    arr.append(key)
print("\n")

print("Printing the Array...")
for x in arr:
    print(x,end=" ")
