"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):  # Reverse second half list
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        first = slow
        cur = slow.next
        last = None
        while cur is not None:
            first.next = last
            last = first
            first = cur
            cur = cur.next
        first.next = last
        while None not in (first, head):
            if first.val != head.val:
                return False
            first = first.next
            head = head.next
        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    a = Solution()
    print(a.isPalindrome(head))
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(a.isPalindrome(head))
