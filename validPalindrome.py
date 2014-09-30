class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        i, j = 0, len(s)-1
        while i < j:
            a = s[i]
            b = s[j]
            if not a.isalnum():
                i += 1
                continue
            if not b.isalnum():
                j -= 1
                continue
            if a != b:
                return False
            i += 1
            j -= 1
        return True
