class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections
        A = A.split()
        B = B.split()
        c_A = collections.Counter(A)
        c_B = collections.Counter(B)
        keys_A = set(c_A.keys())
        keys_B = set(c_B.keys())
        result = []
        for word in keys_A - keys_B:
            if c_A[word] == 1:
                result.append(word)
        for word in keys_B - keys_A:
            if c_B[word] == 1:
                result.append(word)
        return result
