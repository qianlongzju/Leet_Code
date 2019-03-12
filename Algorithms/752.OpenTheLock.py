class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def bfs(lock):
            q, visited = [lock], {lock}
            step = 0
            while q:
                step += 1
                size = len(q)
                for i in range(size):
                    lock = q.pop(0)
                    if target == "".join([str(d) for d in lock]):
                        return step-1
                    for j in range(len(lock)):
                        for diff in [-1, 1]:
                            new_lock = list(lock)
                            new_lock[j] = (new_lock[j] + diff) % 10
                            new_lock = tuple(new_lock)
                            if target == "".join([str(d) for d in new_lock]):
                                return step
                            if "".join([str(d) for d in new_lock]) in deadends:
                                continue
                            if new_lock not in visited:
                                q.append(new_lock)
                                visited.add(new_lock)
            return -1
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        return bfs((0, 0, 0, 0))
