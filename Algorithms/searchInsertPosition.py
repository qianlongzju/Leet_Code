class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low, high = 0, len(A)-1
        while low < high:
            mid = low + (high - low)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                low = mid + 1
            else:
                high = mid
        return (low + 1) if A[low] < target else low
