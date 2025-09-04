class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def modify_node(head, pos, new_data):
    temp = head
    for _ in range(pos):
        if temp is None:
            print("Position out of bounds")
            return head
        temp = temp.next
    if temp:
        temp.data = new_data
    return head

def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before modification:")
display(head)

head = modify_node(head, 1, 99)

print("After modification:")
display(head)

