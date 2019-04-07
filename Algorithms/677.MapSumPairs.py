class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            if c not in node.keys():
                node[c] = {}
            node = node[c]
        node['val'] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c in node.keys():
                node = node[c]
            else:
                return 0
        s = 0
        q = [node]
        while q:
            node = q.pop(0)
            for c in node.keys():
                if c == 'val':
                    s += node['val']
                else:
                    q.append(node[c])
        return s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
