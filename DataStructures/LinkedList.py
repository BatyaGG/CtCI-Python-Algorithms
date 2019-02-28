class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = Node(val)
        self.size += 1

    def append_to_beginning(self, val):
        second_node = self.head
        self.head = Node(val)
        self.head.next = second_node
        self.size += 1

    def append_after_index(self, idx, val):
        if idx >= self.size:
            raise IndexError('index {} is out of bounds'.format(idx))
        curr_node = self.head
        for _ in range(idx):
            curr_node = curr_node.next
        temp_node = curr_node.next
        curr_node.next = Node(val)
        curr_node.next.next = temp_node
        self.size += 1

    def delete_by_index(self, idx):
        if idx >= self.size:
            raise IndexError('index {} is out of bounds'.format(idx))
        self.size -= 1
        if idx == 0:
            self.head = self.head.next
            return
        curr_node = self.head
        for _ in range(idx - 1):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next

    def delete_by_value(self, val):
        if self.size == 0:
            return False
        self.size -= 1
        if self.head.value == val:
            self.head = self.head.next
            return True
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.value == val:
                curr_node.next = curr_node.next.next
                return True
            curr_node = curr_node.next
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        string = '* -> '
        if not self.head:
            return string
        curr_node = self.head
        while curr_node.next is not None:
            string += str(curr_node.value) + ' -> '
            curr_node = curr_node.next
        return string + str(curr_node.value)


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.append(12)
    ll.append(15)
    ll.append(7)
    ll.append_to_beginning(58)
    ll.append_to_beginning(93)
    ll.delete_by_index(0)
    ll.delete_by_index(3)
    print(len(ll))
    print(ll)
    print(ll.delete_by_value(15))
    print(ll)
    ll.append_after_index(1, 14)
    ll.append_after_index(1, 15)
    print(ll)
