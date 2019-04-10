class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.list.append(val)
        if val in self.dict:
            result = False
            self.dict[val].append(len(self.list) - 1)
        else:
            result = True
            self.dict[val] = [len(self.list) - 1]
        return result

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        index = self.dict[val][-1]
        if index != len(self.list) - 1:
            self.list[index] = self.list[-1]
            for i in range(len(self.dict[self.list[-1]])):
                if self.dict[self.list[-1]][i] == len(self.list) - 1:
                    self.dict[self.list[-1]][i] = index
                    break
        self.list.pop()
        self.dict[val].pop(-1)
        if len(self.dict[val]) == 0:
            self.dict.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.list[random.randint(0, len(self.list)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
