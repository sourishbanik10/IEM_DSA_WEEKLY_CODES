class Node:
    def __init__(self, char):
        self.char = char
        self.next = None

def string_to_linked_list(s):
    if not s:
        return None
    head = Node(s[0])
    current = head
    for ch in s[1:]:
        current.next = Node(ch)
        current = current.next
    return head

def display(head):
    while head:
        print(head.char, end=" -> ")
        head = head.next
    print("None")

string = "Sourish"
linked_list = string_to_linked_list(string)
display(linked_list)
