class Node:
    def __init__(self):
        self.elem = None
        self.next = None
        #self.prev = None

class SingleLinkedList():
    def __init__(self):
        self.head = Node()
        self.tail = Node()
    def set(self, data):
        pre_node = Node()
        newNode = Node()
        pre_node.next = newNode
        for i in range(len(data)):
            newNode.elem = data[i]
            newNode = newNode.next
    def empty(self):
        return self.head == None and self.tail == None
    def getSize(self):
        size = 0
        newNode = Node()
        while newNode.next != None:
            newNode = newNode.next
            size += 1
        return size

    def append(self, elem):
        node = Node()
        node.elem = elem
        if (self.getSize() == 0):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def print(self):
        node = Node()
        for i in range(self.getSize()):
            print(node.elem)
            node = node.next
        print(node.elem)
    def insert(self, elem, idx):
        node = Node()
        node.elem = elem

        if self.empty():
            self.head = node
            self.tail = node
        else:
            if idx == 0:
                node.next = self.head
                self.head = node
            elif idx == self.size:
                self.append(node)
            else:
                pre_node = cur_node = self.head
                for i in range(idx):
                    pre_node = cur_node
                    cur_node = cur_node.next
                pre_node.next = node
                node.next = cur_node

    def delete(self, idx):
        pre_node = cur_node = self.head
        if self.empty():
            return False
        elif idx==0:
            if self.getSize() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = cur_node.next
        else:
            for i in range(idx):
                pre_node = cur_node
                cur_node = cur_node.next
            pre_node.next = cur_node.next
            if cur_node == self.tail:
                self.tail = pre_node
if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9]
    s = SingleLinkedList()
    s.set(data)
    s.print()


