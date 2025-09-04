class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

sll = SinglyLinkList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.display()
