class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.max = set()
        self.min = set()

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.data:
            return
        if self.data[key] == 1:
            self.data.pop(key)
        else:
            self.data[key] -= 1

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
