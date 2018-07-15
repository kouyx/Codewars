"""
minimum-number-of-refueling-stops

HARD

汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

Solution2 credit to Olexiy Sadovnikov (saarixx in Leetcode)
"""


class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """


class Solution2:
    def minRefuelStops(self, target, startFuel, stations):
        from collections import defaultdict
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        d = defaultdict(int)
        d[0] = startFuel
        for dist, fuel in stations:
            dd = defaultdict(int)
            stopsNum = 0
            while stopsNum in d:
                if d[stopsNum] >= dist:
                    dd[stopsNum + 1] = d[stopsNum] + fuel
                stopsNum += 1
            for i, j in d.items():
                dd[i] = max(d[i], dd[i])
            d = dd
        stopsNum = 0
        while stopsNum in d:
            if d[stopsNum] >= target:
                return stopsNum
            stopsNum += 1
        return -1


if __name__ == "__main__":
    solu = Solution()
    for i in range(1, 10):
        num = 10 ** i
        print("{}: {} - {}".format(num, bin(num)[2:], solu.reorderedPowerOf2(num)))
