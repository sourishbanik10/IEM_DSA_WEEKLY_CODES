class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, pos):
    if not head:
        print("List is empty")
        return head
    if pos == 0:
        return head.next

    temp = head
    for _ in range(pos - 1):
        if not temp or not temp.next:
            print("Position out of bounds")
            return head
        temp = temp.next

    temp.next = temp.next.next if temp.next else None
    return head

def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before deletion:")
display(head)

head = delete_node(head, 1)

print("After deletion:")
display(head)
