class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        class Digraph(object):
            def __init__(self, v):
                self.v = v
                self.e = 0
                self.adj = [[] for i in range(v)]

            def add_edge(self, v, w):
                self.adj[v].append(w)
                self.e += 1

            def reverse(self):
                r = Digraph(self.v)
                for v in range(self.v):
                    for w in self.adj[v]:
                        r.addEdge(w, v)
                return r

        class DirectedCycle(object):
            def __init__(self, digraph):
                self.marked = [False] * digraph.v
                self.edgeTo = [-1] * digraph.v
                self.cycle = []
                self.onStack = [False] * digraph.v
                for v in range(digraph.v):
                    if not self.marked[v]:
                        self.dfs(digraph, v)

            def dfs(self, digraph, v):
                self.onStack[v] = True
                self.marked[v] = True
                for w in digraph.adj[v]:
                    if self.has_cycle():
                        return
                    elif not self.marked[w]:
                        self.edgeTo[w] = v
                        self.dfs(digraph, w)
                    elif self.onStack[w]:
                        x = v
                        while x != w:
                            self.cycle.insert(0, x)
                            x = self.edgeTo[x]
                        self.cycle.insert(0, w)
                        self.cycle.insert(0, v)
                self.onStack[v] = False

            def has_cycle(self):
                return self.cycle != []

            def get_cycle(self):
                return self.cycle

        digraph = Digraph(numCourses)
        for prerequisite in prerequisites:
            digraph.add_edge(prerequisite[1], prerequisite[0])
        directed_cycle = DirectedCycle(digraph)
        return not directed_cycle.has_cycle()

