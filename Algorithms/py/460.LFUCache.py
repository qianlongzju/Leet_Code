class Node(object):
    def __init__(self, key="", val=-1, freq=-1):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        node = self.data[key]
        node.freq += 1
        while node.prev != self.head and node.freq >= node.prev.freq:
            prev_node, next_node = node.prev, node.next
            prev_node.next, next_node.prev = next_node, prev_node
            prev_node.prev.next, node.prev = node, prev_node.prev
            node.next, prev_node.prev = prev_node, node
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        if key in self.data:
            node = self.data[key]
            node.val = value
            node.freq += 1
            while node.prev != self.head and node.freq >= node.prev.freq:
                prev_node, next_node = node.prev, node.next
                prev_node.next, next_node.prev = next_node, prev_node
                prev_node.prev.next, node.prev = node, prev_node.prev
                node.next, prev_node.prev = prev_node, node
            return

        if self.size == self.capacity:
            node = self.tail.prev
            node.prev.next, self.tail.prev = self.tail, node.prev
            self.data.pop(node.key)
        else:
            self.size += 1
        node = Node(key, value, 1)
        self.data[key] = node
        cur_node = self.tail.prev
        while cur_node.freq == 1:
            cur_node = cur_node.prev
        cur_node.next.prev, node.next = node, cur_node.next
        cur_node.next, node.prev = node, cur_node
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
