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
        self.back

    def append_to_beginning(self, val):
        if self.size == 0:
            self.head = Node(val)
            return
        curr_node = self.head


    def delete_by_index(self, idx):
        pass

    def delete_by_value(self, val):
        pass

