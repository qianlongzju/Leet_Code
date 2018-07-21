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
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ArrayList<Interval> result = new ArrayList<Interval>();
        int i = 0;
        while (i < intervals.size()) {
            if (newInterval.start > intervals.get(i).end) {
                result.add(intervals.get(i));
            } else if (newInterval.end < intervals.get(i).start) {
                break;
            } else {
                if (newInterval.end < intervals.get(i).end) {
                    newInterval.end = intervals.get(i).end;
                }
                if (newInterval.start > intervals.get(i).start) {
                    newInterval.start = intervals.get(i).start;
                }
            }
            i ++;
        }
        result.add(newInterval);
        while (i < intervals.size()) {
            result.add(intervals.get(i));
            i ++;
        }
        return result;
        
    }
}
