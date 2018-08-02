class Solution:
    # @param nums, a list of integers
    # @return a string
    def largestNumber(self, nums):
        nums.sort(cmp=cmp)
        return str(int("".join([str(i) for i in nums])))

def cmp(x, y):
    xx = int(str(x) + str(y))
    yy = int(str(y) + str(x))
    if xx < yy:
        return 1
    elif xx > yy:
        return -1
    else:
        return 0
