class Solution:
    # @param nums, a list of integer
    # @return an integer
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        A = max(nums)
        B = min(nums)
        bucketRange = max(1, int(math.ceil((A - B) / (len(nums) - 1))))
        bucketLen = int(math.ceil((A - B) / bucketRange))
        buckets = [None] * (bucketLen + 1)
        for numsber in nums:
            loc = int(math.ceil((numsber - B) / bucketRange))
            bucket = buckets[loc]
            if bucket:
                bucket['min'] = min(bucket['min'], numsber)
                bucket['max'] = max(bucket['max'], numsber)
            else:
                bucket = {'min':numsber, 'max':numsber}
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
