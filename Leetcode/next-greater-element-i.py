class Stack:
    def __init__(self, init_stack=None):
        if init_stack and isinstance(init_stack, list):
            self.items = init_stack
        else:
            self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]  # return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


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
