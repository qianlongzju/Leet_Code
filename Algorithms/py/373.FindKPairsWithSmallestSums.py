class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = [[n1, n2] for n1 in nums1 for n2 in nums2]
        return heapq.nsmallest(k, q, key=lambda x:x[0]+x[1])
