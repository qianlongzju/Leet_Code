class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        q = []
        k = len(matrix) * len(matrix[0]) - k + 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(q) < k:
                    q.append(matrix[i][j])
                    if len(q) == k:
                        heapq.heapify(q)
                elif matrix[i][j] > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, matrix[i][j])
        return q[0]
