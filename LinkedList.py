# Sam Cole
# This is the linked list class


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        new_node = self.tail.next
        self.tail = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

    def clear(self):
        self.head = None

    def search(self, search):
        current_node = self.head
        while current_node.next or current_node.data == search:
            if current_node.data == search:
                return True
            current_node = current_node.next
        return False

    def delete_node(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
