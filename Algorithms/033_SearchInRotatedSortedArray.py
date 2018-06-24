class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            middle = left + ((right - left) >> 1)
            if target == A[middle]:
                return middle
            elif target == A[left]:
                return left
            elif target == A[right]:
                return right
            elif A[middle] > A[left]:
                if target < A[middle] and target > A[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target > A[middle] and target < A[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
