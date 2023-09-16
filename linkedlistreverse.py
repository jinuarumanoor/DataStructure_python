class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def Insertbegin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def deletebegin(self):
        self.head=self.head.next
    def reverse(self):
        current=self.head
        previous=None
        while current:
            next_node=current.next
            current.next=previous
            previous=current
            current=next_node
        self.head=previous
    def deleteend(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def length(head):
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        return count
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print()
LL1=Linkedlist()
LL1.Insertbegin(30)
LL1.Insertbegin(20)
LL1.Insertbegin(10)
print("orginal Linked list is:")
LL1.display()

print("Reversed Linkedlist is:")
LL1.reverse()
LL1.display()
print("delete from begining linkedlist:")
LL1.deletebegin()
LL1.display()
print("delete from end of linkedlist")
LL1.deleteend()
LL1.display()






