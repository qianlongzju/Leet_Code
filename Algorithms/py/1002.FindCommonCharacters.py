class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        if A == []:
            return []
        import collections
        freq = collections.Counter(A[0])
        freq_keys = set(freq.keys())
        for i in range(1, len(A)):
            freq_keys = freq_keys & set(A[i])
            for c in freq_keys:
                freq[c] = min(freq[c], A[i].count(c))
        result = []
        for k in freq_keys:
            result.extend([k] * freq[k])
        return result
