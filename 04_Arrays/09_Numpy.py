from numpy import *

#ENTERING DATATYPE IN NUMPY ARRAY IS NOT REQUIRED AT ALL...
arr=array([1,"bcd",'e',4,5.6])

for x in arr:
    print(x,end=" ")
print("\n")

#METHOD 2
#arr2=linspace(start,stop,no. of partitions)
arr2=linspace(10,20,5)
for x in arr2:
    print(x,end=" ")
print("\n")

#MEHTOD 3
#arr3=arange(start,stop,step) stop excluded
arr3=arange(10,20,2)
for x in arr3:
    print(x,end=" ")
print("\n")