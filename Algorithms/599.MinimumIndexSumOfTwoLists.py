class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict_1 = {}
        for i, r in enumerate(list1):
            dict_1[r] = i
        min_index_sum = len(list1) - 1 + len(list2) - 1
        result = []
        for i, r in enumerate(list2):
            if r in dict_1:
                if i + dict_1[r] < min_index_sum:
                    result = [r]
                    min_index_sum = i + dict_1[r]
                elif i + dict_1[r] == min_index_sum:
                    result.append(r)
        return result
