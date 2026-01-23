class node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=node(5)
b=node(10)
c=node(15)
d=node(20)
e=node(25)
f=node(30)
g=node(35)

head=a
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=g


print("Printing the LL...")
#traverse
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

#delete the first node
"""
1) node ke first ke head ko 0 krdo
2) head ko next bana do (skips first)
"""
print("Deleted First Node...\n")
head=head.next

curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

#deleting the last node
"""
1) last node ke piche node ko none bana do 
2) while curr.next.next!=None to get 2nd last node.
"""
print("Deleted Last Node..\n")
curr=head
while curr.next.next!=None:
    curr=curr.next

curr.next=None

curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

#Deleting the Kth Nodes
k=2 #2nd element udha denge
curr=head
for i in range(k-1):
    curr=curr.next
curr.next=curr.next.next

curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

