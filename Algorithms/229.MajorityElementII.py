__author__ = 'qianlong'
class Solution:
    # @param nums, a list of integers
    # @return an integer
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for current in nums:
            if current in d:
                d[current] += 1
            elif len(d) < 2:
                d[current] = 1
            else:
                for k in d:
                    d[k] -= 1
                d = dict([(k, v) for k, v in d.items() if v != 0])
        result = []
        for k in d:
            count = sum([1 for n in nums if n == k])
            if count * 1.0 / len(nums) > 1/3.0:
                result.append(k)
        return result
