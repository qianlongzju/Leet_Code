class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return int(math.floor(s.count(letter) * 1.0 / len(s) * 100))
