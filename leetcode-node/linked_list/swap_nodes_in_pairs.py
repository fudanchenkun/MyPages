class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        tmp = head.next
        head.next = head.next.next
        tmp.next = head
        head = tmp

        pre = head.next
        if pre.next is None or pre.next.next is None:
            return head
        first = pre.next.next
        sec = pre.next

        while True:
            sec.next = first.next
            pre.next = first
            first.next = sec

            if sec.next is None or sec.next.next is None:
                break
            sec = sec.next
            first = sec.next
            pre = pre.next.next
        return head