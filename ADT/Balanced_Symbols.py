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


def parChecker(sblStr):
    s = Stack()
    for sbl in sblStr:
        if sbl in '([{':
            s.push(sbl)
        elif sbl in ')]}':
            if s.isEmpty():
                return False
            if not match(s.pop(), sbl):
                return False
    return True if s.isEmpty() else False


def match(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


if __name__ == "__main__":
    print(parChecker('(t){est[ if  i]t w}orks (( with letter ) and digi)t'))
