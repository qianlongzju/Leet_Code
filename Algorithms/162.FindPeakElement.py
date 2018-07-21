class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        return self.findPeakElementInterval(num, 0, len(num)-1)

    def findPeakElementInterval(self, num, start, end):
        if start == end:
            return start
        mid = start + (end - start)/2
        if (mid == 0 or num[mid] > num[mid-1]) and (mid+1 > end or num[mid] > num[mid+1]):
            return mid
        elif (mid == 0 or num[mid] > num[mid-1]) and (mid+1 > end or num[mid] < num[mid+1]):
            return self.findPeakElementInterval(num, mid+1, end)
        else:
            return self.findPeakElementInterval(num, start, end-1)
