class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == []:
            return 0
        ref = collections.defaultdict(int)
        for citation in citations:
            ref[citation] += 1
        for h in range(max(citations), -1, -1):
            if ref[h] >= h:
                return h
            ref[h-1] += ref[h]
    
    def hIndex_sort(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h = i+1
            else:
                break
        return h
