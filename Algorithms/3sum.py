class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = set()
        num = sorted(num)
        n = len(num)
        i = 0
        while i < n:
            while i > 0 and i < n and num[i] == num[i-1]:
                i += 1
            j = i + 1
            k = n - 1
            while j < k:
                total = num[i] + num[j] + num[k]
                if total < 0:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                elif total > 0:
                    k -= 1
                    while k > j and num[k] == num[k+1]:
                        k -= 1
                else:
                    result.add((num[i], num[j], num[k]))
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    k -= 1
                    while k > j and num[k] == num[k+1]:
                        k -= 1
            i += 1
        return [list(a) for a in result]

if __name__ == '__main__':
    num =   [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
    s = Solution()
    r = s.threeSum(num)
    for t in r:
        print t
