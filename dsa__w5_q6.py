class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_beginning(data)
        else:
            tail = self.head.prev
            new_node = Node(data)
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head.prev
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
dcll = DoublyCircularLinkedList()
dcll.insert_at_end(10)
dcll.insert_at_end(20)
dcll.insert_at_end(30)
dcll.insert_at_position(15, 1)
dcll.insert_at_beginning(5)
dcll.display_forward()
dcll.delete_at_position(2)
dcll.delete_at_end()
dcll.delete_at_beginning()
dcll.display_forward()
