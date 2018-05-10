"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        pairs = {'(': ')', '[': ']', '{': '}'}

        for sbl in s:
            if sbl in pairs:
                list1.append(sbl)
            else:
                if not list1 or pairs[list1.pop()] != sbl:
                    return False
        return list1 == []


if __name__ == "__main__":
    a = Solution()
    print(a.isValid('[[]}]'))
