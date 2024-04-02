class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                break
            else:
                if newInterval[1] < intervals[i][1]:
                    newInterval[1] = intervals[i][1]
                if newInterval[0] > intervals[i][0]:
                    newInterval[0] = intervals[i][0]
            i += 1
        result.append(newInterval);
        result.extend(intervals[i:])
        return result