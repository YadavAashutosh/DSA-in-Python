class Node :
    def __init__(self,data):
        self.data = data 
        self.next= None

a= Node(5)
b= Node(7)
c= Node(3)

a.next=b
b.next=c

head=a
print(head.data) #5
print(a.data)#5

print(a.next.data)#7
print(head.next.data)#7

print(a.next.next.data)#

def printlinkedlist(head):
    #tranverse
    curr = head 

    while curr!=None:
        print(curr.data , end=" ")
        curr= curr.next
printlinkedlist(head)  # 5 7 3 
print("")

def insertatfirst(currhead,newdata):
    newnode = Node(newdata)
    newnode.next = currhead
    newhead = newnode
    return newhead

head= insertatfirst(head,10)
printlinkedlist(head) # 10 5 7 3 