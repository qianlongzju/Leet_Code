class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        counts = [(v, key) for key, v in count.items()]
        counts.sort()
        counts.reverse()
        return [key for v, key in counts[:k]]
