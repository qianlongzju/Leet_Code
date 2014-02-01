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
                return True
            elif target == A[left]:
                return True
            elif target == A[right]:
                return True
            elif A[middle] > A[left]:
                if target < A[middle] and target > A[left]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif A[middle] < A[left]:
                if target > A[middle] and target < A[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                left += 1
        return False
