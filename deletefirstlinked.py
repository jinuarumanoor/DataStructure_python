class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_first_node(head):
    if head is None:
        return None

    temporary_node = head
    head = head.next
    del temporary_node

    return head

# Create a linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.next = node3

# Print the linked list before deletion
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print()

# Delete the first node
head = delete_first_node(head)

# Print the linked list after deletion
current = head
while current:
    print(current.data, end=" ")
    current = current.next
print()