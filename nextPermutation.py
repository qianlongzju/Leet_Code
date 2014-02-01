class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num)-1, 0, -1):
            if num[i] <= num[i-1]:
                continue
            for j in range(len(num)-1, i-1, -1):
                if num[j] > num[i-1]:
                    num[i-1], num[j] = num[j], num[i-1]
                    num[i:] = num[i:][::-1]
                    return num
        num = num[::-1]
        return num

if __name__ == '__main__':
    s = Solution()
    print s.nextPermutation([1, 2])
