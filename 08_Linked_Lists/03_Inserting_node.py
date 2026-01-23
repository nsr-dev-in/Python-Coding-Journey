class node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=node(5)
b=node(10)
c=node(15)
head=a
a.next=b
b.next=c

print("Printing the LL...")
print("\n")
#traverse
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

# AT THE BEGINING OF THE LL
print("Inserting at the Begining of the LL...")
print("\n")

newNode=node(1)
newNode.next=head
head=newNode

#traverse
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

# AT THE BEGINING OF THE LL
print("Inserting at the End of the LL...")
print("\n")

newNode2=node(50)

curr=head
while curr.next!=None:
    curr=curr.next

curr.next=newNode2

#traverse
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")

#INSERTING AT THE KTH INDEX
print("Insertion in the Middle oof the LL...")
k=2 #2nd index par krna hai insert
newNode3=node(12)

curr=head
for i in range(k-1):
    curr=curr.next
newNode3.next=curr.next
curr.next=newNode3

#traverse
curr=head
while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next
print("\n")
