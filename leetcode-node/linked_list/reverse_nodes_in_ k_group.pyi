# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def hasKSteps(p):
            p =
            c = 1
            while c < k:
                p = p.next
                c += 1
                if p is None:
                    return False
            return True

        def reverse(pre, head):
            c = 1
            p = head.next
            head.next = None
            np = head
            while c < k and p:
                tmp = p
                p = p.next

                tmp.next = head
                head = tmp
                p = p.next
                c += 1
            if pre:
                pre.next = head
            return p

        if not hasKSteps(head):
            return head
        end = reverse(None, head)
        while end.next:
            end = reverse(end, )
        c = 1
        p = head.next
        head.next = None
        np = head
        while c < k and p:
            tmp = p
            p = p.next

            tmp.next = head
            head = tmp
            p = p.next
            c += 1
        return head