class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, char):
        new_node = Node(char)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def remove_char(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next  # Removing head
                if temp.next:
                    temp.next.prev = temp.prev
                return  # Remove only first occurrence
            temp = temp.next
        print(f"Character '{target}' not found.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
for ch in "HELLO":
    dll.append(ch)
dll.display()
dll.remove_char('L')
dll.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, char):
        new_node = Node(char)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def remove_char(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next  # Removing head
                if temp.next:
                    temp.next.prev = temp.prev
                return  # Remove only first occurrence
            temp = temp.next
        print(f"Character '{target}' not found.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
for ch in "HELLO":
    dll.append(ch)
dll.display()
dll.remove_char('L')
dll.display()
