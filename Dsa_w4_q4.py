class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, data, pos):
    new_node = Node(data)
    if pos == 0:
        new_node.next = head
        return new_node

    temp = head
    for _ in range(pos - 1):
        if temp is None:
            print("Position out of bounds")
            return head
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node
    return head
def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

head = None
head = insert_at_position(head, 10, 0)
head = insert_at_position(head, 20, 1)
head = insert_at_position(head, 15, 1)
display(head)

