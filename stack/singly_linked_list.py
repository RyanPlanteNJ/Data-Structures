class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current_node = self.head

            while current_node.get_next() != self.tail:
                current_node = current_node.get_next()
            self.tail = current_node
            self.tail.set_next(None)
            return value

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_next(new_node)
            self.head.prev = new_node
            self.head = new_node


    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            current_node = self.tail

            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            self.head = current_node
            self.head.set_next(None)
            return value

    def len(self):
        temp = self.head
        count = 0

        while(temp):
            count += 1
            temp = temp.get_next()
        return count

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.get_next()
        return False
