class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self, start):
        prev = None
        current = start
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        return prev  # New head of reversed list

    def divide_and_rejoin(self):
        if not self.head or not self.head.next:
            return

        mid = self.length() // 2
        temp = self.head
        for _ in range(mid - 1):
            temp = temp.next

        second_half = temp.next
        temp.next = None
        if second_half:
            second_half.prev = None

        first_reversed = self.reverse(self.head)
        second_reversed = self.reverse(second_half)

        # Join reversed halves
        self.head = first_reversed
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = second_reversed
        if second_reversed:
            second_reversed.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
for ch in "ABCDEFG":
    dll.append(ch)

print("Original List:")
dll.display()

dll.divide_and_rejoin()

print("After Divide, Reverse, and Rejoin:")
dll.display()
