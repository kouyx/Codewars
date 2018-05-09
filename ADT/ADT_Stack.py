"""
Implement the stack data abstract type in Python using class:
    method list:    O(1) by default
    isEmpty()
    push(item)
    pop()
    peek()
    size()
Reference: pythonds.basic.stack
"""


class Stack:
    def __init__(self, init_stack=None):
        if init_stack and isinstance(init_stack, list):
            self.items = init_stack
        else:
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]  # return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


