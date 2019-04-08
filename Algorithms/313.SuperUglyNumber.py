class Solution:
    def nthSuperUglyNumber_list(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        k = len(primes)
        p = [0] * k
        for i in range(1, n):
            n_u = [ugly[p[j]] * primes[j] for j in range(k)]
            u = min(n_u)
            ugly.append(u)
            for j in range(k):
                if n_u[j] == u:
                    p[j] += 1
        return ugly[-1]
    
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        k = len(primes)
        p = [0] * k
        q = [(ugly[p[j]] * primes[j], j) for j in range(k)]
        heapq.heapify(q)
        while len(ugly) < n:
            u, j = heapq.heappop(q)
            if u > ugly[-1]:
                ugly.append(u)
            p[j] += 1
            heapq.heappush(q, (ugly[p[j]] * primes[j], j))
        return ugly[-1]
