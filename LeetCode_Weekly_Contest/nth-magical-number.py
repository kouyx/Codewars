"""
weekly-contest-95 (7)

nth-magical-number

如果正整数可以被 A 或 B 整除，那么它是神奇的。

返回第 N 个神奇数字。由于答案可能非常大，返回它模 10^9 + 7 的结果。

提示：

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
"""


class Solution:
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """

        def magNum(a, b):
            i = min(a, b)
            yield i
            an = 1 if i == a else 0
            bn = 1 if i == b else 0
            while True:
                a2 = a * (an + 1)
                b2 = b * (bn + 1)
                if a2 > b2:
                    yield b2
                    bn += 1
                else:
                    yield a2
                    an += 1

        for i, ans in enumerate(magNum(A, B)):
            if i == N-1:
                break
        return ans % (10 ** 9 + 7)

