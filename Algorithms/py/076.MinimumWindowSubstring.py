class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needToFind, hasFound = [0] * 256, [0] * 256
        for i in range(len(t)):
            needToFind[ord(t[i])] += 1
        count, begin, end, startIndex = 0, 0, 0, 0
        minLength = len(s)
        while end < len(s):
            if needToFind[ord(s[end])] == 0:
                end += 1
                continue
            hasFound[ord(s[end])] += 1
            if hasFound[ord(s[end])] <= needToFind[ord(s[end])]:
                count += 1
            if count == len(t):
                while needToFind[ord(s[begin])] == 0 or hasFound[ord(s[begin])] > needToFind[ord(s[begin])]:
                    if hasFound[ord(s[begin])] > needToFind[ord(s[begin])]:
                        hasFound[ord(s[begin])] -= 1
                    begin += 1
                length = end - begin + 1
                if length < minLength:
                    minLength = length
                    startIndex = begin
            end += 1
        if count == len(t):
            return s[startIndex:startIndex + minLength]
        else:
            return ""
