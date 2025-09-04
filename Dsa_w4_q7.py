class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

def display(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# List 2: 2 -> 4 -> 6
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

merged = merge_sorted_lists(l1, l2)
reversed_list = reverse_list(merged)

print("Reversed Merged List:")
display(reversed_list)
