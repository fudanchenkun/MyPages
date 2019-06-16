# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        plus = 0
        while p1 and p2:
            tmp = p1.val + p2.val + plus
            if tmp >= 10:
                p1.val = tmp - 10
                plus = 1
            else:
                p1.val = tmp
                plus = 0
            if p1.next is None or p2.next is None:
                break
            p1 = p1.next
            p2 = p2.next
        if p2.next:
            p1.next = p2.next
        if p1.next:
            p1 = p1.next
            while p1 and plus > 0:
                tmp = p1.val + plus
                if tmp >= 10:
                    p1.val = tmp - 10
                else:
                    p1.val = tmp
                    plus = 0
                if p1.next is None:
                    break
                p1 = p1.next
        if plus > 0:
            node = ListNode(1)
            p1.next = node
        return l1