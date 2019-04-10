class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        d = {}
        for i, chars in enumerate(keyboard):
            for c in chars:
                d[c] = i
        result = []
        for word in words:
            if len(set(d[c.lower()] for c in word)) == 1:
                result.append(word)
        return result
