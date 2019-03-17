class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n=len(nums)
        s=sorted(range(n),key=lambda x:nums[x])
        for i in range(n):
            for j in range(i+1,n):
                if abs(s[i]-s[j])<=k:
                    if abs(nums[s[j]]-nums[s[i]])<=t:
                        return True
                    else:
                        break
        return False
