class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        s = s.strip().split()
        return len(s[-1]) if s else 0
