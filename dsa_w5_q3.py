class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

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

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head.prev
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            if temp == self.head.prev:
                break
        print("(tail)")

# Example usage
dcll = DoublyCircularLinkedList()
dcll.append(10)
dcll.append(20)
dcll.append(30)
dcll.display_forward()
dcll.display_backward()
