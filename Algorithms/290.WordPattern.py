class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        inv_d = set()
        str = str.split()
        if len(pattern) != len(str):
            return False
        for p, s in zip(pattern, str):
            if p not in d:
                if s in inv_d:
                    return False
                d[p] = s
                inv_d.add(s)
            else:
                if s != d[p]:
                    return False
        return True
