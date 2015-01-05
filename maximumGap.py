import math
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        A = max(num)
        B = min(num)
        bucketRange = max(1, int(math.ceil((A - B) / (len(num) - 1))))
        bucketLen = int(math.ceil((A - B) / bucketRange))
        buckets = [None] * (bucketLen + 1)
        for number in num:
            loc = int(math.ceil((number - B) / bucketRange))
            bucket = buckets[loc]
            if bucket:
                bucket['min'] = min(bucket['min'], number)
                bucket['max'] = max(bucket['max'], number)
            else:
                bucket = {'min':number, 'max':number}
                buckets[loc] = bucket
        maxGap = 0
        for i in range(len(buckets)):
            if not buckets[i]:
                continue
            j = i + 1
            while j < len(buckets):
                if not buckets[j]:
                    j += 1
                    continue
                maxGap = max(maxGap, buckets[j]['min'] - buckets[i]['max'])
                break
        return maxGap

if __name__ == '__main__':
    s = Solution()
    #print s.maximumGap([1, 10000000])
    #print s.maximumGap([1,1,1,1,1,5,5,5,5,5])
    print s.maximumGap([100,3,2,1])

