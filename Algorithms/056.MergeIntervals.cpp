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
        sort(all(intervals), lesser);
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
int main() {
    Solution s;
    Interval a(1, 3);
    Interval b(2, 6);
    Interval c(8, 10);
    Interval d(15, 18);
    vector<Interval> v;
    v.push_back(a);
    v.push_back(b);
    v.push_back(c);
    v.push_back(d);
    vector<Interval> t = s.merge(v);
    tr(t, it) {
        cout << it->start << " " << it->end << endl;
    }
    return 0;
}
