class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        i, j = 0, len(S)
        for c in S:
            if c == 'I':
                result.append(i)
                i += 1
            else:
                result.append(j)
                j -= 1
        result.append(i)
        return result
