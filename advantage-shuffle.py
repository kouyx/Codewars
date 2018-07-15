"""
advantage-shuffle

给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。

返回 A 的任意排列，使其相对于 B 的优势最大化。

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9


Solution2 credit to Olexiy Sadovnikov (saarixx in Leetcode)
"""


class Solution:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

class Solution2:
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        A = list(sorted(A))
        b = [(v, i) for i, v in enumerate(B)]
        b.sort()
        r = [-1] * n
        used = [False] * n
        i = 0
        for v, j in b:
            while i < n and A[i] <= v:
                i += 1
            if i < n:
                r[j] = A[i]
                used[i] = True
                i += 1
        i = 0
        for j in range(n):
            if used[j]: continue
            while r[i] >=0:
                i += 1
            r[i] = A[j]
            i += 1
        return r

if __name__ == "__main__":
    solu = Solution()
    for i in range(1, 10):
        num = 10 ** i
        print("{}: {} - {}".format(num, bin(num)[2:], solu.reorderedPowerOf2(num)))
