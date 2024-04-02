class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, nums):
        result = 0
        for i in range(32):
            tmp = 0
            bitOps = 1 << i
            for j in nums:
                j = j if j > 0 else -j
                if j & bitOps:
                    tmp += 1
            result += (tmp % 3) << i
        flag = sum(1 for i in nums if i < 0)
        return result * (-1 if flag % 3 else 1)
