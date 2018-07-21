class Solution {
public:
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
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
int main() {
    Solution s;
    vector<Interval> v;
    v.push_back(Interval(1, 3));
    v.push_back(Interval(6, 9));
    v = s.insert(v, Interval(2, 5));
    for (int i=0; i < v.size(); i++) {
        cout << v[i].start << " " << v[i].end << endl;
    }
    cout << endl;
    v.clear();
    v.push_back(Interval(1, 2));
    v.push_back(Interval(3, 5));
    v.push_back(Interval(6, 7));
    v.push_back(Interval(8, 10));
    v.push_back(Interval(12, 16));
    v = s.insert(v, Interval(4, 9));
    for (int i=0; i < v.size(); i++) {
        cout << v[i].start << " " << v[i].end << endl;
    }
    cout << endl;
    v.clear();
    v = s.insert(v, Interval(5, 7));
    for (int i=0; i < v.size(); i++) {
        cout << v[i].start << " " << v[i].end << endl;
    }
    cout << endl;
    return 0;
}

