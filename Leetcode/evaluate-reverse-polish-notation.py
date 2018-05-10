"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
"""

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opstack = []
        for x in tokens:
            if x not in '+-*/':
                opstack.append(int(x))
            else:
                rt = opstack.pop()
                lf = opstack.pop()
                if x == '+':
                    opstack.append(lf + rt)
                elif x == '-':
                    opstack.append(lf - rt)
                elif x == '*':
                    opstack.append(lf * rt)
                else:
                    opstack.append(int(lf / rt))
        return opstack.pop()


if __name__ == "__main__":
    a = Solution()
    print(a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
