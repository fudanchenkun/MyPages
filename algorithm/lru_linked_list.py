class Node(object):
    def __init__(self, key, value):
        self.pre = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.items = {}

    def getTail(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp

    def updateLinkedList(self, node):
        if node.key != self.head.key:
            node.pre.next = node.next
            if node.next:
                node.next.pre = node.pre
            node.pre = None
            node.next = self.head
            self.head.pre = node
            self.head = node

    def printLinkedList(self):
        tmp = self.head
        ans = ''
        while tmp:
            ans += str(tmp.key)
            tmp = tmp.next
        print(ans)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items:
            node = self.items[key]
            # print 'get', key
            self.updateLinkedList(node)
            return self.head.value
        # self.printLinkedList()
        # print self.items.keys()
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print 'put', key, value
        if key in self.items:
            node = self.items[key]
            self.updateLinkedList(node)
            node.value = value
        else:
            if len(self.items) >= self.capacity:
                tail = self.getTail()
                if tail.pre:
                    tail.pre.next = None
                tail.pre = None
                del self.items[tail.key]
            node = Node(key, value)
            node.next = self.head
            if self.head:
                self.head.pre = node
            self.items[key] = node
            self.head = node
        # self.printLinkedList()
        # print self.items.keys()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)