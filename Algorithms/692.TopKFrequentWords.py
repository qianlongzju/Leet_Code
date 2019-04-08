class Solution:
    def topKFrequent_sort(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        r = sorted(c.items(), key=lambda x:(-x[1], x[0]))[:k]
        return [x[0] for x in r]
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        r = heapq.nsmallest(k, c.items(), key=lambda x: (-x[1], x[0]))
        #r = heapq.nlargest(k, c.items(), key=lambda x: (x[1], x[0]))
        return [x[0] for x in r]
        #q = []
        #for key, value in c.items():
        #    if len(q) < k:
        #        q.append((value, key))
        #        if len(q) == k:
        #            heapq.heapify(q)
        #    elif value > q[0][0]:
        #        heapq.heappop(q)
        #        heapq.heappush(q, (value, key))
        #result = []
        #while q:
        #    result.append(heapq.heappop(q)[1])
        #return result
