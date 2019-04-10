class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        c = collections.Counter(s)
        return "".join([t[0]*t[1] for t in sorted(c.items(), key=lambda x:x[1], reverse=True)])
