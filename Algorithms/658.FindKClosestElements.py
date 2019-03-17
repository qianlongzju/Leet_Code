class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i, j = 0, len(arr) - k -1
        while i <= j:
            #print len(arr), i, j
            mid = i + ((j - i) // 2)
            if x - arr[mid] > arr[mid+k] - x:
                i = mid + 1
            elif x - arr[mid] == arr[mid+k] - x:
                if mid == 0 or arr[mid] != arr[mid-1]:
                    i = mid
                    break
                else:
                    j = mid - 1
            else:
                j = mid - 1
        return arr[i:i+k]
