"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2dict = {}
        stack = []
        for num2 in nums2:
            while stack and stack[-1] < num2:
                nums2dict[stack.pop()] = num2
            stack.append(num2)
        ans = []
        for num1 in nums1:
            ans.append(nums2dict.get(num1, -1))
        return ans


if __name__ == "__main__":
    a = Solution()
    print(a.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
