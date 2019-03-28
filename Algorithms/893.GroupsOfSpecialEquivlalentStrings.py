class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d = collections.defaultdict(list)
        for s in A:
            key = sorted(s[::2]) + sorted(s[1::2])
            d[tuple(key)].append(s)
        return len(d)
