class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [0] * len(graph)
        for i in range(len(graph)):
            if color[i] == 0 and not self.dfs(graph, color, i):
                return False

    def dfs(self, graph, color, i):
        color[i] = 1
        q = [i]
        while q:
            i = q.pop(0)
            for neighbor in graph[i]:
                if color[neighbor] == 0:
                    q.append(neighbor)
                    color[neighbor] = -color[i]
                elif color[neighbor] == color[i]:
                    return False
        return True
