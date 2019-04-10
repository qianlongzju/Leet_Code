public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
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
        List<Interval> result = new ArrayList<>();
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
