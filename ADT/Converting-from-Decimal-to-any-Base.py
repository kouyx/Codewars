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


def divideBy2(decNumber):
    digits = []
    while decNumber > 0:
        digits.append(str(decNumber % 2))
        decNumber = decNumber // 2
    # a little slower way:
    # binString = ""
    # while digits != []:
    #     binString += digits.pop()
    binString = "".join(digits[::-1])
    return binString


def baseConverter(decNumber, base):
    digit = "0123456789ABCDEF"
    digits = []
    while decNumber > 0:
        digits.append(digit[decNumber % base])
        decNumber = decNumber // base
    newString = "".join(digits[::-1])
    return newString


if __name__ == "__main__":
    print(divideBy2(42))
    print(baseConverter(25, 2))
    print(baseConverter(25, 16))
