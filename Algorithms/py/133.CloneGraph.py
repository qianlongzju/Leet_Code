"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        if not node: return None
        copyNode = Node(node.val, [])
        mapping = {node: copyNode}
        queue = [node]
        while queue:
            curr = queue.pop(0)
            copyCurr = mapping[curr]
            for neighbor in curr.neighbors:
                if neighbor in mapping:
                    copyCurr.neighbors.append(mapping[neighbor])
                else:
                    copyNeighbor = Node(neighbor.val, [])
                    queue.append(neighbor)
                    mapping[neighbor] = copyNeighbor
                    copyCurr.neighbors.append(copyNeighbor)
        return copyNode

    def cloneGraph_dfs(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.mapping = {}
        if not node: return None
        return self.dfs(node)

    def dfs(self, node):
        if node in self.mapping: return self.mapping[node]
        copyNode = Node(node.val, [])
        self.mapping[node] = copyNode
        for neighbor in node.neighbors:
            copyNode.neighbors.append(self.dfs(neighbor))
        return copyNode
