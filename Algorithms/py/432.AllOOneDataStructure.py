class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.head = Node("", -1)
        self.tail = Node("", -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        if key not in self.data:
            node = Node(key, 1)
            self.data[key] = node
            node.next, node.prev = self.head.next, self.head
            self.head.next.prev = node
            self.head.next = node
        else:
            node = self.data[key]
            node.val += 1
            while node.next != self.tail and node.val > node.next.val:
                next_node, prev_node = node.next, node.prev
                node.next = next_node.next
                node.next.prev = node
                node.prev = next_node
                next_node.next = node
                prev_node.next = next_node
                next_node.prev = prev_node

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.data:
            return
        node = self.data[key]
        if node.val == 1:
            prev_node, next_node = node.prev, node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.data.pop(key)
        else:
            node.val -= 1
            while node.prev != self.head and node.val < node.prev.val:
                next_node, prev_node = node.next, node.prev
                prev_node.prev.next = node
                node.prev = prev_node.prev
                node.next = prev_node
                prev_node.prev = node
                prev_node.next = next_node
                next_node.prev = prev_node

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.tail.prev != self.head:
            return self.tail.prev.key
        return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head.next != self.tail:
            return self.head.next.key
        return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
