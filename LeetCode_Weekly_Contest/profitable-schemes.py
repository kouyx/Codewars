"""
weekly-contest-95 (7)

profitable-schemes

帮派里有 G 名成员，他们可能犯下各种各样的罪行。

第 i 种犯罪会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。

让我们把这些犯罪的任何子集称为盈利计划，该计划至少产生 P 的利润。

有多少种方案可以选择？因为答案很大，所以返回它模 10^9 + 7 的值。

提示：

1 <= G <= 100
0 <= P <= 100
1 <= group[i] <= 100
0 <= profit[i] <= 100
1 <= group.length = profit.length <= 100
"""


class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        