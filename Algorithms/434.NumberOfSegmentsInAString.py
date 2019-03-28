class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for w in s.split(" "):
            if w != '':
                count += 1
        return count
