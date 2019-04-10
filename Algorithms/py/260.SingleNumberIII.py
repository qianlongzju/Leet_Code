class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        r = 0
        for num in nums:
            r ^= num
        bit = 1
        while r & bit == 0:
            bit <<= 1
        a, b = 0, 0
        for num in nums:
            if num & bit != 0:
                a ^= num
            else:
                b ^= num
        return [a, b]
