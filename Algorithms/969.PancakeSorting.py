class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        result = []
        for i in range(n):
            maximum, index = A[0], 0
            for j in range(1, n-i):
                if A[j] > maximum:
                    maximum, index = A[j], j
            if index == n-i-1:
                continue
            result.append(index+1)
            result.append(n-i)
            A[:index+1] = A[:index+1][::-1]
            A[:n-i] = A[:n-i][::-1]
        return result
