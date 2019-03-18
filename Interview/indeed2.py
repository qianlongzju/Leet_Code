#Input:
#  - m lists of sorted and distinct integers
#  - k (integer)
#Output: the top k integers that occur the most frequently

#Example:

#Input:
#    m = [
#      [2, 3, 6],
#      [1, 3, 4, 5, 6, 8],
#      [1, 3, 5, 6, 9, 10],
#      [3, 5, 7, 11]
#    ]
#    k = 3
    
#    OUTPUT: [3, 5, 6]
# [2, 1, 1, 3] -> 1 is the min -> [2, 1, 3] -> [2, 1, 3, 3] -> [2, 3, 3, 3] -> 1 occurs 2 times -> 
#--- Write code below here ---

def func_sorted(m, k):
    import heapq
    q = []
    row_index = [1] * len(m)
    for i in range(len(m)):
        q.append((m[i][0], i))
    #time: o(row)
    #space: o(row)
    heapq.heapify(q)
    prev, freq = None, 0
    q_freq = []
    # time: o(n*log(row))
    # space: o(row) + o(k)
    while q:
        val, row = heapq.heappop(q)
        if prev == None:
            prev = val
            freq = 1
        elif val == prev:
            freq += 1
        else:
            if len(q_freq) < k:
                q_freq.append((freq, prev))
                if len(q_freq) == k:
                    heapq.heapify(q_freq)
            elif freq > q_freq[0][0]:
                heapq.heappop(q_freq)
                heapq.heappush(q_freq, (freq, prev))
            prev = val
            freq = 1
        if row_index[row] < len(m[row]):
            heapq.heappush(q, (m[row][row_index[row]], row))
            row_index[row] += 1
    else:
        if len(q_freq) < k:
            q_freq.append((freq, prev))
            if len(q_freq) == k:
                heapq.heapify(q_freq)
        elif freq > q_freq[0][0]:
            heapq.heappop(q_freq)
            heapq.heappush(q_freq, (freq, prev))
    result = []
    print(len(q_freq))
    while q_freq:
        v, key = heapq.heappop(q_freq)
        result.append(key)
    # time & space: o(k)
    return result

def func(m, k):
    import collections
    d = collections.defaultdict(int)
    for row in m:
        for i in row:
            d[i] += 1
    # o(n)
    # o(x) x is the distinct number
    q = []
    import heapq
    for key, v in d.items():
        if len(q) < k:
            q.append((v, key))
            if len(q) == k:
                heapq.heapify(q)
        else:
            if v > q[0][0]:
                heapq.heappop(q)
                heapq.heappush(q, (v, key))
    # n*log(k)
    # space o(k)
    result = []
    print(len(q))
    while q:
        v, key = heapq.heappop(q)
        result.append(key)
    # k*log(k)
    # o(k)
    return result
    # nlog(k)
    # o(x) 
m = [
      [2, 3, 6],
      [1, 3, 4, 5, 6, 8],
      [1, 3, 5, 6, 9, 10],
      [3, 5, 7, 11]
    ]  
k = 3
print(func(m, k))

print(func_sorted(m, k))
