"""
LIST FUNCTIONS

MAX()
MIN()
SLICING
COUNT()
SORT()
REVERSE()
COPY()
INDEX()
"""

list1=[1,2,1,31,1,4,5]

# MAX MIN FUNCTION ORDER OF N TIME COMPLEXITY
print(min(list1))
print(max(list1))

# COUNT -- NO. OF OCCURENCE 
print(list1.count(1)) 

# SORT THE LSIT
list1.sort() # O(NLOGN)
print(list1) # INSCREASING ORDER

# REVERSING THE LIST
list1.reverse()
print(list1) # DESCRISING ORDER

# INDEX -- RETURN INDEX OF AN ELEMENT
print(list1.index(31))