import java.util.*;
public class Solution {
    public int longestConsecutive(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        HashSet<Integer> m = new HashSet<Integer>();
        for (int i=0; i < num.length; ++i) {
            m.add(num[i]);
        }
        int longestLength = 0;
        for (int i=0; i < num.length; ++i) {
            int j = num[i];
            int length = 1;
            while (m.contains(j+1)) {
                m.remove(j+1);
                j ++;
                length ++;
            }
            j = num[i];
            while (m.contains(j-1)) {
                m.remove(j-1);
                j --;
                length ++;
            }
            if (length > longestLength) {
                longestLength = length;
            }
        }
        return longestLength;
    }
}
