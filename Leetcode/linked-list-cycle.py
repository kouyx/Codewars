class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


class Solution(object):
    def hasCycle(self, head):
        """
        hash
        :type head: ListNode
        :rtype: bool
        """
        hash1 = set([])
        while head and head.next:
            if head in hash1:
                return True
            else:
                hash1.add(head)
                head = head.next
        return False
