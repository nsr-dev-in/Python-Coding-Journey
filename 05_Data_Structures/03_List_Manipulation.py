list1=[12,24,36,48,60]
list2=list1

print(list1)
print(list2)

list2.append(100)
print(list1,id(list1))
print(list2,id(list2))