class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if isPalindrome(s):
            return True
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s[i+1:j+1]) or isPalindrome(s[i:j])
            i += 1
            j -= 1
