# Sam Cole
# this is the Queue class First in First out
from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.add_to_head(data)

    def pop(self):
        self.myList.remove_head()
