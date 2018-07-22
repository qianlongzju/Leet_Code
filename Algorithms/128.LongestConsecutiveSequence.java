public class Solution {
    public int longestConsecutive(int[] num) {
        Set<Integer> m = new HashSet<>();
        for (int i: num)
            m.add(i);
        int longestLength = 0;
        for (int i: num) {
            int length = 1;
            for (int j=i+1; m.contains(j); j++) {
                m.remove(j);
                length ++;
            }
            for (int j=i-1; m.contains(j); j--) {
                m.remove(j);
                length ++;
            }
            longestLength = Math.max(longestLength, length);
        }
        return longestLength;
    }
}
