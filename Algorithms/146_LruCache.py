class Node(object):
    def __init__(self, k=None, v=None):
        self.key = k
        self.value = v
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity, self.size = capacity, 0
        self.m = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            p = self.m[key]
            p.next.pre = p.pre
            p.pre.next = p.next
            p.next = self.head.next
            self.head.next.pre = p
            p.pre = self.head
            self.head.next = p
            return p.value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.m:
            p = self.m[key]
            p.next.pre = p.pre
            p.pre.next = p.next
            p.next = self.head.next
            self.head.next.pre = p
            p.pre = self.head
            self.head.next = p
            p.value = value
        else:
            p = Node(key, value)
            p.next = self.head.next;
            self.head.next.pre = p
            p.pre = self.head
            self.head.next = p
            self.m[key] = p
            self.size += 1
            if self.size > self.capacity:
                p = self.tail.pre
                p.pre.next = self.tail
                self.tail.pre = p.pre
                del self.m[p.key]
                self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
