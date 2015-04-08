# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        copyNode = UndirectedGraphNode(node.label)
        mapping = {node: copyNode}
        queue = [node]
        while queue:
            curr = queue.pop(0)
            copyCurr = mapping[curr]
            for neighbor in curr.neighbors:
                if neighbor in mapping:
                    copyCurr.neighbors.append(mapping[neighbor])
                else:
                    copyNeighbor = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                    mapping[neighbor] = copyNeighbor
                    copyCurr.neighbors.append(copyNeighbor)
        return copyNode

    ## dfs
    #mapping = {}
    #def cloneGraph(self, node):
    #    if not node: return None
    #    return self.dfs(node)

    #def dfs(self, node):
    #    if node in self.mapping: return self.mapping[node]
    #    copyNode = UndirectedGraphNode(node.label)
    #    self.mapping[node] = copyNode
    #    for neighbor in node.neighbors:
    #        copyNode.neighbors.append(self.dfs(neighbor))
    #    return copyNode
