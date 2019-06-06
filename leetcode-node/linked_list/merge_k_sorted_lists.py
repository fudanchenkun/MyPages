class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        heaptree = []
        for j in range(len(lists)):
            if not lists[j] is None:
                heapq.heappush(heaptree, (lists[j].val, lists[j]))

        if len(heaptree) <= 0:
            return None
        item = heapq.heappop(heaptree)
        head = item[1]
        p = head
        if p.next:
            heapq.heappush(heaptree, (p.next.val, p.next))
        p.next = None
        while len(heaptree) > 0:
            # print heaptree
            item = heapq.heappop(heaptree)
            p.next = item[1]
            if p.next.next:
                heapq.heappush(heaptree, (p.next.next.val, p.next.next))
            p = p.next
            p.next = None
        return head