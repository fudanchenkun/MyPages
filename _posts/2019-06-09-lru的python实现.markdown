# 2019-06-09-lru实现

- 在整理redis笔记和刷leetcode的时候都遇到了LRU（Least Recently Used）算法，就把它的实现整理了一下。
- 这个算法貌似可以用在很多地方，除了redis的过期策略，百度了下内存管理中的页面置换算法和缓存方面也有应用。

## 思路

算法的目的就是淘汰做不常使用的数据（或者什么的吧），主要思路就是双向列表+字典：
- 双向列表记录每个数据项使用顺序，最新添加的（put方法）和最新获取的（get方法）否放在表头，表尾就是最不常使用的数据项。
- 字典的作用就是在o(1)的复杂度下获取数据 
- 还要有个capacity用于限制数据量的大小

## 最简单的实现 

collections.OrderedDict是python的有序列表，使用它实现最便捷，下面的代码是直接从书上抄下了的。
```python
from collections import OrderedDict
class LRUDict(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        old_value = self.items.get(key)
        if old_value is not None:
            self.items.pop(key)
            self.items[key] = value
        elif len(self.items) < self.capacity:
            self.items[key] = value
        else:
            self.items.popitem(last=True)
            self.items[key] = value

    def __getitem__(self, key):
        value = self.items.get(key)
        if value is not None:
            self.items.pop(key)
            self.items[key] = value
        return value

    def __repr__(self):
        return repr(self.items)
```

## 直接使用list实现
lru实现起来并不复杂，可以作为面试题，百度就出过。作为面试题，直接使用库实现，显然不会被接受。尝试用了下python的list实现，但效率惨不忍睹，在LeetCode中只超过了5.2%，勉强accpet。
```python
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keyList = []
        self.items = {}
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items.keys():
            self.keyList.remove(key)
            self.keyList.insert(0,key)
            return self.items[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.items.keys():
            self.keyList.remove(key)
            self.keyList.insert(0,key)
            self.items[key] = value
        else:
            if len(self.keyList) >= self.capacity:
                last_key = self.keyList.pop()
                del self.items[last_key]
            self.keyList.insert(0, key)
            self.items[key] = value 
```

## 双向列表的实现
list效率低的原因正是在把元素移到表头这一步（list是顺序存储，在执行时头插时把后面的每个数据项都往后挪一次），而lru使用场景中最频繁的操作也就是要把数据项移到表头。改用链表无疑是必须的。
实现如下
```python
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
```

确实效率提高了不少，但在上面的实现中，我没有设置尾节点的指针，因此在删除节点时会比较耗时，主要是因为尾结点的指针貌似不好维护，我就偷懒了。
这个solution只击败了不到30%，还是有必要设置一个tail指针的。
