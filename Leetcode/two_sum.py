"""
hash-table
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i, x in enumerate(nums):
            v = target - x
            if v in dict1:
                return [dict1[v], i]
            dict1[x] = i
        return []


if __name__ == "__main__":
    a=Solution()
    print(a.twoSum([2,7,11,15], 9))