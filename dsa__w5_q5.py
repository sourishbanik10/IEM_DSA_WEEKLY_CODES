class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp:
            print("Position out of bounds")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        if not temp.next:
            self.head = None
            return
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos):
            if not temp:
                print("Position out of bounds")
                return
            temp = temp.next
        if not temp:
            print("Position out of bounds")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_position(15, 1)
dll.insert_at_beginning(5)
dll.display()
dll.delete_at_position(2)
dll.delete_at_end()
dll.delete_at_beginning()
dll.display()
