public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new ArrayList<>();
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
