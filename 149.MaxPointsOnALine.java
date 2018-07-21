public class Solution {
    public int maxPoints(Point[] points) {
        int size = points.length;
        if (size <= 2)
            return size;
        HashMap<Double, Integer> slopeMap = new HashMap<Double, Integer>();
        int maxCount = 0;
        for (int i=0; i < size; ++i) {
            int duplicates = 1;
            int vertical = 0;
            slopeMap.clear();
            for (int j=0; j < size; ++j) {
                if (i == j)
                    continue;
                if (points[i].x == points[j].x && points[i].y == points[j].y) {
                    duplicates ++;
                    continue;
                }
                if (points[i].x == points[j].x)
                    vertical ++;
                else {
                    double k = (points[i].y - points[j].y) * 1.0 / (points[i].x - points[j].x);
                    if (!slopeMap.containsKey(k))
                        slopeMap.put(k, 1);
                    else 
                        slopeMap.put(k, slopeMap.get(k) + 1);
                }
            }
            for(int value: slopeMap.values())
                if (value > vertical)
                    vertical = value;
            if (vertical + duplicates > maxCount)
                maxCount = vertical + duplicates;
        }
        return maxCount;
    }
    // public static double epsilon = .0001;
    // public static double floorToNearestEpsilon(double d) {
    //     int r = (int) (d / epsilon);
    //     return ((double) r) * epsilon;
    // }
    // public int maxPoints(Point[] points) {
    //     // IMPORTANT: Please reset any member data you declared, as
    //     // the same Solution instance will be reused for each test case.
    //     int bestCount = 0;
    //     HashMap<Double, ArrayList<Line>> linesBySlope = 
    //             new HashMap<Double, ArrayList<Line>>();
    //     
    //     for (int i = 0; i < points.length; i++) {
    //         for (int j = i+1; j < points.length; j++) {
    //             Line line = new Line(points[i], points[j]);
    //             insertLine(linesBySlope, line);
    //             int count = countEquivalentLines(linesBySlope, line);
    //             if (count > bestCount) {
    //                 bestCount = count;
    //             }
    //         }
    //     }
    //     return bestCount;
    // }
    // int countEquivalentLines(ArrayList<Line> lines, Line line) {
    //     if (lines == null) return 0;
    //     int count = 0;
    //     for (Line parallelLine : lines)
    //         if (parallelLine.isEquivalent(line))
    //             count ++;
    //     return count;
    // }
    // int countEquivalentLines(
    //         HashMap<Double, ArrayList<Line>> linesBySlope, Line line) {
    //     double key = floorToNearestEpsilon(line.slope);
    //     double eps = epsilon;
    //     int count = countEquivalentLines(linesBySlope.get(key), line) + 
    //             countEquivalentLines(linesBySlope.get(key - eps), line) +
    //             countEquivalentLines(linesBySlope.get(key + eps), line);
    //     return count;
    // }
    // void insertLine(HashMap<Double, ArrayList<Line>> linesBySlope, Line line) {
    //     ArrayList<Line> lines = null;
    //     double key = floorToNearestEpsilon(line.slope);
    //     if (!linesBySlope.containsKey(key)) {
    //         lines = new ArrayList<Line>();
    //         linesBySlope.put(key, lines);
    //     } else {
    //         lines = linesBySlope.get(key);
    //     }
    //     lines.add(line);
    // }
    // class Line {       
    //     public double slope, intercept;
    //     private boolean infinite_slope = false;
    //     public Line(Point p, Point q) {
    //         if (Math.abs(p.x - q.x) > epsilon) {
    //             slope = (p.y - q.y) / (p.x - q.x);
    //             intercept = p.y - slope * p.x;
    //         } else {
    //             infinite_slope = true;
    //             intercept = p.x;
    //         }
    //     }
    //     
    //     public boolean isEquivalent(double a, double b) {
    //         return (Math.abs(a - b) < epsilon);
    //     }
    //     
    //     public boolean isEquivalent(Object o) {
    //         Line l = (Line) o;
    //         if (isEquivalent(l.slope, slope) &&
    //                 isEquivalent(l.intercept, intercept) &&
    //                 (infinite_slope == l.infinite_slope)) {
    //             return true;
    //         }
    //         return false;
    //     }
    // }
}
