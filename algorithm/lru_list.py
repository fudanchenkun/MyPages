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