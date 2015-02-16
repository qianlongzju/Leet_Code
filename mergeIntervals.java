import java.util.*;
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public ArrayList<Interval> merge(ArrayList<Interval> intervals) {
        if (intervals.size() <= 1) {
            return intervals;
        }
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval a,  Interval b) {
                if(a.start == b.start)
                    return a.end - b.end;
                return a.start - b.start;
            }
        });
        ArrayList<Interval> result = new ArrayList<Interval>();
        Interval v = intervals.get(0);
        int i = 1;
        while (i < intervals.size()) {
            if (v.end >= intervals.get(i).start) {
                if (intervals.get(i).end > v.end) {
                    v.end = intervals.get(i).end;
                }
            } else {
                result.add(v);
                v = intervals.get(i);
            }
            i ++;
        }
        result.add(v);
        return result;
    }
}
