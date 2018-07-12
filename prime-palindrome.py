"""
# 回文素数 prime-palindrome

求出大于或等于 num 的最小回文素数。

回顾一下，如果一个数大于 1，且其因数只有 1 和它自身，那么这个数是素数。

例如，2，3，5，7，11 以及 13 是素数。

回顾一下，如果一个数从左往右读与从右往左读是一样的，那么这个数是回文数。

例如，12321 是回文数。

1 <= num <= 10^8

"""


class Solution:
    def primePalindrome(self, num):
        """
        :type num: int
        :rtype: int
        """

        def isPrime(num):
            if num % 2 == 0:
                return False
            for x in range(3, int(num ** 0.5) + 1, 2):
                if num % x == 0:
                    return False
            return True

        def isPalindrome(num):
            ns = str(num)
            return ns == ns[::-1]

        def nextPalindrome(num):
            ns = str(num)
            if set(ns) == {'9'}:
                return num + 2
            nl = len(ns)
            if ns[0] in ('2', '4', '5', '6', '8'):
                hg = int(ns[0])
                while hg not in (3, 7, 9):
                    hg += 1
                return int("{0}{1}{0}".format(hg, '0' * (nl - 2)))
            if isPalindrome(num):
                num += 2
                ns = str(num)
            ls = ns[:nl // 2]
            rs = ns[-(nl // 2):]
            if nl % 2 == 0:
                # 偶数位
                for l, r in zip(ls[::-1], rs):
                    if l > r:
                        return int(ls + ls[::-1])
                    elif l < r:
                        ls = str(int(ls) + 1)
                        return int(ls + ls[::-1])
            else:
                # 奇数位
                mid = ns[nl // 2]
                for l, r in zip(ls[::-1], rs):
                    if l > r:
                        return int(ls + mid + ls[::-1])
                    elif l < r:
                        lsm = str(int(ls + mid) + 1)
                        return int(lsm + lsm[-2::-1])

        if num <= 101:
            for x in (2, 3, 5, 7, 11, 101):
                if num <= x:
                    return x
        if num % 2 == 0:
            num += 1
        if not isPalindrome(num):
            num = nextPalindrome(num)
        while not isPrime(num):
            num = nextPalindrome(num)
        return num


class Solution2:
    def primePalindrome(self, num):
        """
        :type num: int
        :rtype: int
        """

        def isPrime(num):
            if num < 2 or num % 2 == 0:
                return num == 2

            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        if num <= 101:
            for x in (2, 3, 5, 7, 11, 101):
                if num <= x:
                    return x
        for i in range(10 ** (int(len(str(num)) // 2)), 10 ** 5):
            digit = int(str(i) + str(i)[-2::-1])
            if digit >= num and isPrime(digit):
                return digit


if __name__ == "__main__":
    solu = Solution()
    solu2 = Solution2()
    for i in range(1, 13):
        print("{}: {}".format(i, solu2.primePalindrome(i)))
    print(solu.primePalindrome(10000300000))
