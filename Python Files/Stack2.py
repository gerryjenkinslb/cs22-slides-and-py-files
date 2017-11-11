# version of stack where first item in list is the top of stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)  # changed

    def pop(self):
        return self.items.pop(0)  # changed

    def peek(self):
        return self.items[0]  # changed

    def size(self):
        return len(self.items)


