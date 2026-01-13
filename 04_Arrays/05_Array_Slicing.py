from array import *
arr=array("i",[2,4,6,8,10])


#traversing in array
for x in arr:
    print(x,end=" ")
print("\n")


#METHOD 1 POSITIVE INDEXING
arr2=arr[1:5] #1 se 4 tk ke elements ayge bas last include nhi hota usme
for x in arr2:
    print(x,end=" ")
print("\n")


#METHOD 2 STARTING KE ELEMENTS CHAIYE LEKIN LAST KE ELEMENTS NHI CHAIYE
arr3=arr[0:-2] #last 2 elements excluded 
for x in arr3:
    print(x,end=" ")