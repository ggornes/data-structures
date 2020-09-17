class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None

    """ Insert a new node at start """
    def insert_at_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    """ Insert a new node at the end """
    def insert_at_end(self, data):

        # check if list is empty insert new element
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return

        # if not empty, traverse to find the last node
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_node = Node(data)
        current_node.next = new_node
        new_node.prev = current_node

    """ Insert a new node after another node """
    def insert_after_node(self, element, data):
        # check if empty
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == element:
                    # found element to be inserted after
                    break
                current_node = current_node.next

            # element was not in the list
            if current_node is None:
                print("Element not found")

            else:
                new_node = Node(data)
                new_node.prev = current_node
                new_node.next = current_node.next

                # if current node is not the last node
                if current_node.next is not None:
                    # assign current node prev reference
                    current_node.prev = new_node

                # assign current node_next reference
                current_node.next = new_node

    """ Insert a new node before another node """
    def insert_before_node(self, element, data):
        # check if empty
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.data == element:
                    break
                current_node = current_node.next
            if current_node is None:
                print("Element not found")
            else:
                new_node = Node(data)
                new_node.next = current_node
                new_node.prev = current_node.prev
                if current_node.prev is not None:
                    current_node.prev.next = new_node
                current_node.prev = new_node

    def traverse_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next

    def delete_start(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            # if only one element
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.prev.next = None

    def delete_element(self, element):
        # if list is empty
        if self.head is None:
            print("The list is empty")
            return

        # if list has only one element
        if self.head.next is None:
            if self.head.data == element:
                self.head = None
            else:
                print("Element not found")
            return

        # list is not empty but the element to be deleted is the first element on the list
        if self.head.data == element:
            self.head = self.head.next
            self.head.prev = None
            return

        # if not empty and not the first element, traverse
        current_node = self.head
        while current_node is not None:
            if current_node.data == element:
                break
            current_node = current_node.next

            if current_node.next is not None:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
            else:
                if current_node.data == element:
                    current_node.prev.next = None
                else:
                    print("Element not found")

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def display(self):
        for node in self:
            print(node.data)

    def reverse_linked_list(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        p = self.head
        print(p.data, " -> p")
        q = p.next
        print(q.data, " -> q")
        p.next = None
        p.prev = q
        while q is not None:
            print(q.data, "p: ")
            print(q.data, "q: ")
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.head = p

    def reverse_list(self):
        temp_node = None
        current_node = self.head

        # Swap next and prev for all nodes of
        # doubly linked list
        while current_node is not None:
            temp_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp_node
            current_node = current_node.prev

            # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp_node is not None:
            self.head = temp_node.prev

if __name__ == "__main__":
    dl = DLinkedList()
    dl.insert_at_end(1)
    dl.insert_at_end(2)
    dl.insert_at_end(3)
    dl.insert_at_end(4)



    dl.display()

    dl.reverse_list()
    dl.display()



