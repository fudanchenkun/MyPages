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
            if p is None:
                return False
            c = 1
            while c < k:
                p = p.next
                c += 1
                if p is None:
                    return False
            return True

        def reverse(head):
            c = 1
            nh = head.next
            head.next = None
            end = head
            while c < k:
                tmp = nh
                nh = nh.next
                tmp.next = head
                head = tmp
                c += 1
            return head, end, nh

        if k <= 1:
            return head
        if not hasKSteps(head):
            return head
        head, end, nh = reverse(head)
        while True:
            if not hasKSteps(nh):
                end.next = nh
                break

            part_head, part_end, nh = reverse(nh)
            end.next = part_head
            end = part_end
        return head