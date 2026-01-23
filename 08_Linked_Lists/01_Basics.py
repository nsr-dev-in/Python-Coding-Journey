"""
1) LINKED LIST IS A USER DEFINED DATA STRUCTURE.
2) NODE -- DATA INFORMATION STORE. (WE DEFINE THIS NODE)
3) POINTER -- TO THE NEXT NODE.
4) Class -- Blueprint 
5) Object -- class ka object attribute
"""

# HOW TO CREATE A LINKED LIST

#CLASS BLUEPRINT
class node:
    def __init__(self,data):
        self.data=data #store data in linked list
        self.next=None

#object bana diya class ka
a=node(5)
b=node(7)
c=node(9)

a.next=b
b.next=c

#Representing the Linked List
head=a

# c.next by default None hai kiska last next
    
print(head.data) #a
print(head.next.data) #b 
print(head.next.next.data) #c



