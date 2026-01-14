"""
LIST -- ORDERED INDEXED MUTABLE DUBLICATES

len()
negative indexing
append()
extend()
remove()
pop()
insert()
clear()
"""

name=["Nitin","Rohit","Sam","Meena","Nitin"]

#OPERATIONS ON LISTS
# 1 ACCESSING LIST ELEMENTS
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# NEGATIVE INDEXING
print(name[-1])
print(name[-3])

# 2 MUTABLE
name[4]="Rupesh"
print(name[4])

# 3 LEN() -- NO. OF ELEMENTS RETURN
print(len(name))

# 4 APPEND() -- ADD ELEMENT AT LAST OF THE LIST
name.append("1000")
print(name[5])

name.append([10,20,30])
print(name)

# 5 EXTEND() -- ADD THE ELEMENTS OF THE LIST INTO THE LIST
name.extend([1,2,3,4,5,6])
print(name)

# 6 INSERT() -- ADD ELEMENT AT THAT INDEX , with VALUE 
name.insert(2,"Rupa")
print(name)

# 7 REMOVE() -- REMOVE THE ELEMENT BY VALUE
name.remove("Rupa")
print(name)

# 8 POP() -- REMOVE THE ELEMENT BY INDEXING / LAST ELEMENT
name.pop()
print(name)

name.pop(-1) #last element
print(name)

# 9 CLEAR() -- CLEAR THE WHOLE LIST
name.clear()
print()