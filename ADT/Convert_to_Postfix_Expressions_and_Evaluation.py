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


def infixToPostfix(infixexpr):
    postfixList = []
    opstack = []
    prec = {}
    prec['('] = 1
    prec['+'] = prec['-'] = 2
    prec['*'] = prec['/'] = 3
    list1 = infixexpr.split()
    for x in list1:
        if x.isalnum():
            postfixList.append(x)
        elif x == '(':
            opstack.append(x)
        elif x == ')':
            top = opstack.pop()
            while top != '(':
                postfixList.append(top)
                top = opstack.pop()
        else:
            while opstack and prec[opstack[-1]] >= prec[x]:
                postfixList.append(opstack.pop())
            opstack.append(x)
    while opstack:
        postfixList.append(opstack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    postlist = postfixExpr.split()
    opstack = []
    for x in postlist:
        if x.isdigit():
            opstack.append(int(x))
        else:
            opstack.append(doMath(x, opstack.pop(), opstack.pop()))
    return opstack.pop()


def doMath(op, op2, op1):
    if op == '+':
        return op1 + op2
    if op == '-':
        return op1 - op2
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    return None


if __name__ == "__main__":
    print(infixToPostfix("A * B + C * D"))
    print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(postfixEval('7 8 + 3 2 + /'))
