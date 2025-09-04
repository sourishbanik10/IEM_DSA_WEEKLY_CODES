class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def left_slide(head, k):
    if not head or k == 0:
        return head

    # Find the length of the list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head
    temp = head
    for _ in range(k - 1):
        temp = temp.next

    new_head = temp.next
    temp.next = None
    tail.next = head
    return new_head

def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original List:")
display(head)

k = 2
head = left_slide(head, k)

print(f"List after left sliding by {k} nodes:")
display(head)
