class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
        self.size += 1

    def append_to_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append_to_index(self, idx, val):
        if idx > self.size or idx < 0:
            raise IndexError('Index {} is out of bounds'. format(idx))
        new_node = Node(val)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            for _ in range(idx - 1):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
        self.size += 1

    def pop_first(self):
        if self.size == 0:
            return None
        pop_val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return pop_val

    def pop_last(self):
        if self.size == 0:
            return None
        if self.size == 1:
            pop_val = self.head.value
            self.head = None
            self.size -= 1
            return pop_val
        curr_node = self.head
        for _ in range(self.size - 2):
            curr_node = curr_node.next
        pop_val = curr_node.next.value
        curr_node.next = None
        self.size -= 1
        return pop_val

    def pop_by_index(self, idx):
        if idx >= self.size or idx < 0:
            raise IndexError('Index {} is out of bounds'.format(idx))
        if idx == 0:
            pop_val = self.head.value
            self.head = self.head.next
            self.size -= 1
            return pop_val
        curr_node = self.head
        for _ in range(idx - 1):
            curr_node = curr_node.next
        pop_val = curr_node.next.value
        curr_node.next = curr_node.next.next
        self.size -= 1
        return pop_val

    def pop_by_value(self, val):
        if self.size == 0:
            return None
        if self.head.value == val:
            pop_val = self.head.value
            self.head = self.head.next
            self.size -= 1
            return pop_val
        curr_node = self.head
        while curr_node.next is not None and curr_node.next.value != val:
            curr_node = curr_node.next
        if curr_node.next:
            curr_node.next = curr_node.next.next
            self.size -= 1
            return val
        return None

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
    ll.append(8)
    ll.append(9)
    ll.append_to_beginning(1)
    ll.append_to_beginning(0)
    ll.append_to_index(4, 23)
    print(ll)
    print(ll.pop_by_value(9))
    print(ll.pop_by_value(12))
    print(ll.pop_by_value(5))
    print(ll.pop_by_value(0))
    print(ll)
    print(len(ll))
