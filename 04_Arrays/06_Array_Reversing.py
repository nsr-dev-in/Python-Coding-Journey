from array import *

arr=array("i",[1,2,3,4,5])
print("Original Array...")
for x in arr:
    print(x,end=" ")
print("\n")

#copying rev of arr in another arr
rev_arr=arr[::-1]
print("Reversed Array...")
for x in rev_arr:
    print(x,end=" ")