"""
reordered-power-of-2

从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

1 <= N <= 10^9

Solution2 credit to Olexiy Sadovnikov (saarixx in Leetcode)
"""


class Solution:
    def reorderedPowerOf2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ns = str(num)
        nl = sorted(ns)
        power2 = []
        decMax = 10 ** len(ns)
        power2max = len(bin(decMax)) - 2
        power2min = len(bin(decMax // 10)) - 3
        # find power of 2 in [10**(len(ns)-1), 10**(len(ns)))
        for i in range(power2min, power2max):
            power2.append(sorted(str(2 ** i)))
        # sort and compare with every power of 2
        for s in power2:
            if s == nl:
                return True
        return False


class Solution2:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        d1 = sorted(str(N))
        for i in range(0, 30):
            d2 = sorted(str(1 << i))
            if d1 == d2:
                return True
        return False


if __name__ == "__main__":
    solu = Solution2()
    for i in range(0, 21):
        num = 1 if i == 0 else i * 2
        print("{}: {}".format(num, solu.reorderedPowerOf2(num)))
