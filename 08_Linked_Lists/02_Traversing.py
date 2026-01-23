"""
How to Traverse in the LL ?
1) make a pointer curr.
2) curr ko head de do
3) jab tk mera curr is not equal to last address  none 
4) tb tk apka curr ka data print krna hai 
5) then curr ko curr ke next address de dena hai so it can move to the next
"""

#STRUCTURE BASE OF LINKED LIST
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#CREATING VALUE DATA OF LL
a=node(2)
b=node(4)
c=node(6)
d=node(8)
e=node(10)

#NODE LINKING
head=a
a.next=b
b.next=c
c.next=d
d.next=e

#curr ek pointer hai 
curr=head 

while curr!=None:
    print(curr.data,end=" ")
    curr=curr.next #pointer me ek agge jana hai 

