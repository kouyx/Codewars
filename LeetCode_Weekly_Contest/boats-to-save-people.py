"""
weekly-contest-96 (5)

boats-to-save-people

第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

输入：people = [1,2], limit = 3
输出：1

输入：people = [3,2,2,1], limit = 3
输出：3

输入：people = [3,5,3,4], limit = 5
输出：4

"""


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        