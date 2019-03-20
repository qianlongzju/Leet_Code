class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str 
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        n = len(start)
        i, j = 0, 0
        while i < n and j < n:
            while i < n and start[i] == 'X': 
                i += 1
            while j < n and end[j] == 'X': 
                j += 1
            if i == n or j == n:
                break
            if start[i] != end[j]:
                return False
            if start[i] == 'R' and i > j:
                return False
            if start[i] == 'L' and i < j:
                return False
            i += 1
            j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True
