class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort()
        n = len(people)
        result = [[] for i in range(n)]
        for i in range(n):
            h, k = people[i]
            count = 0
            for j in range(n):
                if result[j] == [] or result[j][0] >= h:
                    count += 1
                if count == k + 1:
                    result[j] = [h, k]
                    break
        return result
