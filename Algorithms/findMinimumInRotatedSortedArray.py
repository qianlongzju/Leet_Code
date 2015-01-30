class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return self.findMin_interval(num, 0, len(num) - 1)
    def findMin_interval(self, num, start, end):
        if start == end:
            return num[start]
        if num[start] < num[end]:
            return num[start]
        mid = start + (end - start) / 2
        if num[mid] >= num[start]:
            return self.findMin_interval(num, mid+1, end)
        return self.findMin_interval(num, start, mid)

if __name__ == '__main__':
    s = Solution()
    print s.findMin([1])
