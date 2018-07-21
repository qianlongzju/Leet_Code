class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        if not s:
                return ""
        s = s.split()
        s.reverse()
        return " ".join(s)
