/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool lesser(const Interval& a, const Interval& b) {
        if(a.start == b.start)
            return a.end < b.end;
        return a.start < b.start;
    }
    vector<Interval> merge(vector<Interval> &intervals) {
        if (intervals.size() <= 1) {
            return intervals;
        }
        sort(intervals.begin(), intervals.end(), lesser);
        vector<Interval> result;
        Interval v = intervals[0];
        int i = 1;
        while (i < intervals.size()) {
            if (v.end >= intervals[i].start) {
                if (intervals[i].end > v.end) {
                    v.end = intervals[i].end;
                }
            } else {
                result.push_back(v);
                v = intervals[i];
            }
            i ++;
        }
        result.push_back(v);
        return result;
    }
};
