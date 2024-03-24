class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                m = sum(1 for num in nums[i:j] if num % p == 0)
                #print(nums[i:j], m)
                if m <= k:
                    res.add(tuple(nums[i:j]))
        #print(res)
        return len(res)
        
