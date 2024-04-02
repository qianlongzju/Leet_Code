class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        start = 0
        result = []
        for end in range(1, len(nums)):
            if nums[end] != nums[end-1]+1:
                if end - 1 == start:
                    result.append(str(nums[start]))
                else:
                    result.append("{}->{}".format(nums[start], nums[end-1]))
                start = end
        else:
            if start == end:
                result.append(str(nums[end]))
            else:
                result.append("{}->{}".format(nums[start], nums[end]))
        return result
        