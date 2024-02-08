class Node:
    def __init__(self):
        self.elem = None
        self.next = None
        #self.prev = None

class SingleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0

        self.head = None
        self.tail = None
    def insert(self, elem, idx):
        node = Node()
        node.elem = elem

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if idx == 0:
                node.next = self.head
                self.head = node
            else:
                cur_node = self.head
                for i in range(idx):
                    node


