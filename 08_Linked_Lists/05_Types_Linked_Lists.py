"""
1) SINGLY LL (DATA -- NEXT)
2) DOUBLY LL (PREVIOUS -- DATA -- NEXT)
3) CIRCULAR LL (None last pointer points to head pointer) -- if curr==head : break
"""

                            #DOUBLY LL
class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

#DATA 
a=node(2)
b=node(3)
c=node(4)
d=node(5)
e=node(6)

#HEAD
head=a

#NEXT POINTER
a.next=b
b.next=c
c.next=d
d.next=e

#PREVIOUS NODE
b.prev=a
c.prev=b
d.prev=c 
e.prev=d 

#TRAVERSING
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

                    #CIRCULAR LL
class node2:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

#DATA 
a2=node2(12)
b2=node2(13)
c2=node2(14)
d2=node2(15)
e2=node2(16)

#HEAD
head=a2

#NEXT POINTER
a2.next=b2
b2.next=c2
c2.next=d2
d2.next=e2
e2.next=a2

#PREVIOUS NODE
b2.prev=a2
c2.prev=b2
d2.prev=c2 
e2.prev=d2 

curr=head

while True:
    print(curr.data,end=" ")
    curr=curr.next
    if curr==head:
        break
print("\n")


