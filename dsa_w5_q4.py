class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                print("Position out of bounds")
                return
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            prev = None
            temp = self.head
            while temp.next != self.head:
                prev = temp
                temp = temp.next
            prev.next = self.head

    def delete_at_position(self, pos):
        if not self.head:
            print("List is empty")
            return
        if pos == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next
            if temp.next == self.head:
                print("Position out of bounds")
                return
        temp.next = temp.next.next

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
cll = SinglyCircularLinkedList()
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_position(15, 1)
cll.insert_at_beginning(5)
cll.display()
cll.delete_at_position(2)
cll.delete_at_end()
cll.delete_at_beginning()
cll.display()
