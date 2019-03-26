class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = [sum(a for a in A if a&0x01==0)]
        for val, index in queries:
            if A[index]&0x01 == 1 and val&0x01 == 1:
                result.append(result[-1] + A[index] + val)
            elif A[index]&0x01 == 0 and val&0x01 == 1:
                result.append(result[-1] - A[index])         
            elif A[index]&0x01 == 0 and val&0x01 == 0:
                result.append(result[-1] + val)
            else:
                result.append(result[-1])
            A[index] += val
        return result[1:]
