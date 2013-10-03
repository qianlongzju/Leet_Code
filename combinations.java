import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        ArrayList<ArrayList<Integer> > result = new ArrayList<ArrayList<Integer>>();
        for (int i=0; i < Math.pow(2, n); i++) {
            ArrayList<Integer> v = new ArrayList<Integer>();
            int j = i;
            int p = 1;
            int q = 0;
            while (j != 0) {
                if ((j & 0x01) != 0) {
                    v.add(p);
                    q ++;
                }
                p ++;
                j >>= 1;
            }
            if (k == q) {
                result.add(v);
            }
        }
        return result;
    }
}
