# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def quickSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swep(pre, first, node):
            tmp = node.next
            node.next = tmp.next
            if pre is None:
                tmp.next = first
                head = tmp
                first = tmp
            else:
                tmp1 = pre.next
                pre.next = tmp
                tmp.next = tmp1
            return pre, first
        def quicksort(pre, first, l):
            if first is None:
                return None
            flag_node = first
            flag = first.val
            p = first
            c = 0
            i = 0
            while p.next and i < l:
                if p.next.val < flag:
                    pre, first = swep(pre, first, p)
                    c += 1
                    i += 1
                p = p.next
                i += 1
            quicksort(pre, first, c)
            quicksort(p, p.next, l - c)

        if head is None:
            return head
        list_len = 0
        t = head
        while t:
            t = t.next
            list_len += 1
        quicksort(None, head, list_len)

        return head


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        ans = head
        head = head.next
        p = ans
        p.next = None
        while head:
            p = ans
            if head.val <= p.val:
                ans = head
                head = head.next
                ans.next = p
            else:
                while p.next and p.next.val < head.val:
                    p = p.next
                if p.next is None:
                    p.next = head
                    head = head.next
                    p = p.next
                    p.next = None
                else:
                    tmp = p.next
                    p.next = head
                    head = head.next
                    p = p.next
                    p.next = tmp
        return ans


    def mergeSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return Solution.sort(head)

    @staticmethod
    def sort(head):
        # 归并排序适合单链表
        # 分治、合并
        if head is None or head.next is None:
            return head
        first = head.next
        sec = head
        while first.next:
            if first.next.next:  # 注意一个指针先行的时候判断走第二步的时候是否为None
                first = first.next.next
                sec = sec.next
            else:
                first = first.next
        mid = sec.next
        sec.next = None
        # print mid.next.val
        return Solution.merge(Solution.sort(head), Solution.sort(mid)) # 核心

    @staticmethod
    def merge(l1, l2):  # 两个列表合并
        # if l1 is None:
        #     return l2
        # if l2 is None:
        #     return l1
        if l1.val <= l2.val:
            tmp = l1
            l1 = l1.next
        else:
            tmp = l2
            l2 = l2.next
        head = tmp
        tmp.next = None
        p = head
        while l1 and l2:
            if l1.val <= l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            p.next = tmp
            tmp.next = None
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head







def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)

            ret = Solution().sortList(head)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()