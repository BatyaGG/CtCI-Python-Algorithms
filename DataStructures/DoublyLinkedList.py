class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.back = None
        self.size = 0

    def append(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.back = self.head
        else:
            new_node = Node(val)
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node
        self.size += 1

    def append_to_beginning(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.back = self.head
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete_by_index(self, idx):
        pass

    def delete_by_value(self, val):
        pass

