class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        length_list = [1] * n
        result = 0
        for i in range(n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    length_list[i] = max(length_list[i], length_list[j]+1)
            result = max(result, length_list[i])
        return result


    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            pos = self.search(result, nums[i])
            #print(pos)
            if pos == len(result):
                result.append(nums[i])
            else:
                result[pos] = nums[i]
            #print(result)
        return len(result)

    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if mid == 0 or nums[mid-1] <= target:
                    return mid
                high = mid
            else:
                if mid == len(nums)-1 or nums[mid+1] >= target:
                    return mid+1
                low = mid + 1
        return low
