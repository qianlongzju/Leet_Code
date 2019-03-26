class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if S == None or len(S) <= 1:
            return []
        prev = S[0]
        start = 0
        result = []
        for i in range(1, len(S)):
            if S[i] != prev:
                if i-start >= 3:
                    result.append([start, i-1])
                prev = S[i]
                start = i
        if len(S) - start >= 3:
            result.append([start, len(S)-1])
        return result
