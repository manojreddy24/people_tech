class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insertNodeAtTail(self, head, data):
        new_node = Node(data)
        if head is None:
            return new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            return head

# Create a new linked list
linked_list = Linked_list()

# Input the number of nodes
list_count = int(input("Enter the number of nodes: "))

# Insert nodes into the linked list
for i in range(list_count):
    data = int(input("Enter node data: "))
    linked_list.head = linked_list.insertNodeAtTail(linked_list.head, data)

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Print the linked list
print("The linked list is:")
print_linked_list(linked_list.head)
