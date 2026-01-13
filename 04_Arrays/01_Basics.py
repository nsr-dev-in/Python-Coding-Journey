#TO USE ARRAY IN PYTHON  1) WE USE NUMPY 2) IN BUILT MODULE

#Implementation of Array...
import array
#METHOD 1
#array_variable=array.array("type_of_array",[array_data])
val=array.array("i",[1,3,5,7,9,11])
print(val)

#METHOD 2
"""
import array as ar
arr=ar.array("i",[1,2,3,4,5])
"""

#METHOD 3
"""
from array import *
arr=array("i",[1,2,3,4,5])
"""

#TRAVERSING ARRAY
#METHOD 1
for i in range(0,6):
    print(val[i],end=" ")

#METHOD 2
print()
for x in val:
    print(x,end=" ")