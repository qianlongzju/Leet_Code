class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        result = 1
        for i in range(1, n+1):
            result *= (2*n-i+1)*1.0/i;
        result /= n+1
        return int(result)

    """
    def numTrees(self, n):
        num = [0 for i in range(n+1)]
        num[0] = 1
        for i in range(1, n+1):
            num[i] = 0
            for j in range(1, i+1):
                num[i] += num[j-1]*num[i-j];
        return num[n]
    """
