class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        import collections
        c = collections.Counter(deck)
        num = min(c.values())
        if num == 1:
            return False
        import fractions
        d = num
        for k, v in c.items():
            d = fractions.gcd(d, v)
        return d != 1
