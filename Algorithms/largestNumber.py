class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num.sort(cmp=cmp)
        return str(int("".join([str(i) for i in num])))

def cmp(x, y):
    xx = int(str(x) + str(y))
    yy = int(str(y) + str(x))
    if xx < yy:
        return 1
    elif xx > yy:
        return -1
    else:
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.largestNumber([3, 30, 34, 5, 9]) == '9534330'
    print s.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247])
