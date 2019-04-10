class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def compare(word1, word2):
            l1, l2 = len(word1), len(word2)
            for i in range(min(l1, l2)):
                order1, order2 = order.index(word1[i]), order.index(word2[i])
                if order1 < order2:
                    return -1
                elif order1 > order2:
                    return 1
            return l1 - l2
        for i in range(1, len(words)):
            if compare(words[i-1], words[i]) > 0:
                return False
        return True
