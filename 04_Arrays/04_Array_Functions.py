from array import *
arr=array("i",[10,20,30,40,50])


#TYPE CODE OF AN ARRAY...
print("Type Code of an Array : ",arr.typecode)
print("\n")


#REVERSING AN ARRAY...
arr.reverse()
print("Reversed Array : ")
for x in arr:
    print(x,end=" ")
print("\n")


#INSERTION IN ARRAY...
#insertion hogi indexing ke based par
arr.insert(3,25)
print("Insertion done at index 3: ")
for x in arr:
    print(x,end=" ")
print("\n")


#insertion hogi last me 
arr.append(5)
print("Insertion done in last : ")
for x in arr:
    print(x,end=" ")
print("\n")


#copying an array...
arr2=array(arr.typecode,(x for x in arr))
print("Array Copied From Array 1 :")
for x in arr2:
    print(x,end=" ")
print("\n")


#Deletion in array USING POP (INDEX)...
arr2.pop(2)
print("30 Value Deleted From Array 2 using INDEX :")
for x in arr2:
    print(x,end=" ")
print("\n")


#Deletion in array USING REMOVE (VALUE)...
arr2.remove(50)
print("50 Value Deleted From Array 2 using Value Deletion :")
for x in arr2:
    print(x,end=" ")