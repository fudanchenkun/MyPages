"""
指向头结点的时候就算走一步了
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        n -= 1
        while n > 0:
            first = first.next
            n -= 1
        if first.next is None:
            head = head.next
            return head
        second = head
        first = first.next
        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return head