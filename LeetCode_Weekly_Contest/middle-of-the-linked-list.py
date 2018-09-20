"""
weekly-contest-95 (3)

middle-of-the-linked-list

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

给定链表的结点数介于 1 和 100 之间。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head.next
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
        return slow
