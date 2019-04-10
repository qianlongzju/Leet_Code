class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        for k in r:
            if k not in m or m[k] < r[k]:
                return False
        return True
