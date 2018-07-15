"""
给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。

如果没有两个连续的 1，返回 0 。

1 <= N <= 10^9

输入：22
输出：2
解释：
22 的二进制是 0b10110 。
在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
第一对连续的 1 中，两个 1 之间的距离为 2 。
第二对连续的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。

Solution2 credit to Olexiy Sadovnikov (saarixx in Leetcode)
"""


class Solution:
    def binaryGap(self, num):
        """
        :type num: int
        :rtype: int
        """
        binStr = bin(num)[2:]
        gap = 0
        last = 0
        for i, s in enumerate(binStr[1:], 1):
            if s == '1':
                gaps = i - last
                if gaps > gap:
                    gap = gaps
                last = i
        return gap


class Solution2:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        seen = False
        n = 0
        r = 0
        while N > 0:

            if N & 1 == 1:
                if not seen:
                    seen = True
                else:
                    r = max(r, n)
                    n = 0
            N >>= 1
            if seen:
                n += 1
        return r


if __name__ == "__main__":
    solu = Solution()
    for i in range(1, 10):
        num = 10 ** i
        print("{}: {} - {}".format(num, bin(num)[2:], solu.binaryGap(num)))
