from card import Card

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        if not self.head:
            self.head = Node(data)
            return
        for current_node in self:
            pass
        current_node.next = Node(data)

    def delete(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head

        for node in self:
            # node.data.print()
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def search(self, item):
        for node in self:
            # print("Item: '%s'" % item)
            # if isinstance(item, Card):
            #     item.pprint()
            # print("node: '%s'" % node.data)
            # if isinstance(node.data, Card):
            #     node.data.pprint()
            if node.data == item:
                print ("card found")
                return node
        print("Card not found")
        return None

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    """ add the same behavior to linked lists as a normal list """
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    """ Traverse: going through every single node, starting with the head of the linked list and ending on the node 
    that has a next value of None. """
    def display(self):
        # current = self.head
        # while current is not None:
        #     print(current)
        #     current = current.next
        for node in self:
            # print(node.data)
            if isinstance(node.data, Card):
                """ In this case, we know data is a Card so we can use Card.print() """
                node.data.print()
            else:
                print(node.data)

    """ pretty display: print card in a card shape"""
    def pdisplay(self):
        for node in self:
            # print(node)
            node.data.pprint()

    """ group display: group cards by card suit (♥♦♣♠)"""
    def gdisplay(self):
        print("--- Cards grouped by suit: ---")
        H = []
        D = []
        S = []
        C = []
        H_string = '♥'
        D_string = '♦'
        S_string = '♣'
        C_string = '♠'

        for node in self:
            # node.data.pprint()
            # print (node.data.suit)
            if node.data.suit == 'H':
                H.append(node.data)
                H_string += '-' + str(node.data.rank)
            if node.data.suit == 'D':
                D.append(node.data)
                D_string += '-' + str(node.data.rank)
            if node.data.suit == 'S':
                S.append(node.data)
                S_string += '-' + str(node.data.rank)
            if node.data.suit == 'C':
                C.append(node.data)
                C_string += '-' + str(node.data.rank)

        print(H_string)
        print(D_string)
        print(S_string)
        print(C_string)




