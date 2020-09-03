class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def display(self):
        for node in self:
            node.data.print()
