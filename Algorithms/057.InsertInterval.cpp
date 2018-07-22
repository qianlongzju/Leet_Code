class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        vector<Interval> result;
        int i = 0;
        while (i < intervals.size()) {
            if (newInterval.start > intervals[i].end) {
                result.push_back(intervals[i]);
            } else if (newInterval.end < intervals[i].start) {
                break;
            } else {
                if (newInterval.end < intervals[i].end) {
                    newInterval.end = intervals[i].end;
                }
                if (newInterval.start > intervals[i].start) {
                    newInterval.start = intervals[i].start;
                }
            }
            i ++;
        }
        result.push_back(newInterval);
        while (i < intervals.size()) {
            result.push_back(intervals[i]);
            i ++;
        }
        return result;
    }
};
