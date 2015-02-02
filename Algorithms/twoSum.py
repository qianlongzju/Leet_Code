class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mapping = {}
        for i in range(len(num)):
            mapping[num[i]] = i
        for i in range(len(num)):
            gap = target - num[i]
            if gap in mapping and mapping[gap] != i:
                break
        return (i + 1, mapping[gap] + 1)
