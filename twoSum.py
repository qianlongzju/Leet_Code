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

    #def twoSum(self, num, target):
    #    sorted_num = sorted(num)
    #    n = len(num)
    #    i, j = 0, n-1
    #    while i < j:
    #        t = sorted_num[i] + sorted_num[j]
    #        if t == target:
    #            i = num.index(sorted_num[i])
    #            j = num.index(sorted_num[j])
    #            if j == i:
    #                j = i + 1 + num[i+1:].index(sorted_num[j])
    #            r = (i + 1, j + 1)
    #            return (min(r), max(r))
    #        elif t < target:
    #            i += 1
    #        else:
    #            j -= 1

