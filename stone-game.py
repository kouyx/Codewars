"""
stone-game

亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

亚历克斯先手

提示：
2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。
"""


class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        def pickStone(piles):
            if len(piles) <= 2:
                return 0 if piles[0] > piles[-1] else -1
            else:
                big = sum(piles) // len(piles) * 2
                if piles[0] < piles[-1]:
                    return -1 if piles[-2] < big else 0
                else:
                    return 0 if piles[1] < big else -1

        win = sum(piles) // 2
        alex, lee = 0, 0
        for i in range(len(piles) // 2):
            pick = pickStone(piles)
            alex += piles.pop(pick)
            pick = pickStone(piles)
            lee += piles.pop(pick)
            if alex > win:
                return True
            if lee > win:
                return False
        return alex > lee


if __name__ == "__main__":
    solu = Solution()
    li = [[6, 9, 4, 3, 9, 8], [8, 9, 7, 6, 7, 6]]
    for piles in li:
        print("{}".format(piles))
        print("{}".format(solu.stoneGame(piles)))
