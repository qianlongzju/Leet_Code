class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        self.result, self.path, m = [], [], {}
        q, level, maxLevel = [start], {start:1}, -1
        visited = set()
        visited.add(start)
        while q:
            tmp = q.pop(0)
            if maxLevel != -1 and level[tmp] > maxLevel:
                break;
            for i in range(len(tmp)):
                for c in string.lowercase:
                    if c == tmp[i]: continue
                    temp = tmp[:i] + c + tmp[i+1:]
                    if temp == end:
                        maxLevel = level[tmp]
                        if not end in m:
                            m[end] = []
                        m[end].append(tmp)
                    elif temp in dict:
                        if not temp in visited:
                            q.append(temp)
                            visited.add(temp)
                            m[temp] = [tmp]
                            level[temp] = level[tmp] + 1
                        elif level[tmp]+1 == level[temp]:
                            m[temp].append(tmp)
        self.buildPaths(start, end, m)
        return self.result

    def buildPaths(self, start, end, m):
        if start == end:
            self.result.append([start] + self.path[:])
            return
        self.path.insert(0, end)
        if end in m:
            for i in range(len(m[end])):
                self.buildPaths(start, m[end][i], m)
        self.path.pop(0)
