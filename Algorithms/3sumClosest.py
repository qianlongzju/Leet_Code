class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        result = set()
        num = sorted(num)
        n = len(num)
        i = 0
        closestSum = num[0] + num[1] + num[2]
        min_gap = abs(closestSum - target)
        while i < n:
            while i > 0 and i < n and num[i] == num[i-1]:
                i += 1
            j = i + 1
            k = n - 1
            while j < k:
                total = num[i] + num[j] + num[k]
                gap = abs(total - target)
                if gap < min_gap:
                    closestSum = total
                    min_gap = gap
                if total < target:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                elif total > target:
                    k -= 1
                    while k > j and num[k] == num[k+1]:
                        k -= 1
                else:
                    return closestSum
            i += 1
        return closestSum
