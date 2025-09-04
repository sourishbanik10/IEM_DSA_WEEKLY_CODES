class Node:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.next = None

def insert(head, height, weight):
    new_node = Node(height, weight)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

def max_ratio(head):
    max_r = 0
    while head:
        if head.height != 0:
            ratio = head.weight / head.height
            if ratio > max_r:
                max_r = ratio
        head = head.next
    return max_r


n = int(input("Enter number of students: "))
head = None
for _ in range(n):
    h = float(input("Enter height: "))
    w = float(input("Enter weight: "))
    head = insert(head, h, w)

print("Max weight/height ratio:", max_ratio(head))
