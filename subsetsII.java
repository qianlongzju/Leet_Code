import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> subsetsWithDup(int[] S) {
        Arrays.sort(S);        
        int n = S.length;
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> uniqueResult = new HashSet<ArrayList<Integer>>();
        for (int i=0; i < Math.pow(2, n); i++) {
            ArrayList<Integer> v = new ArrayList<Integer>();
            int j = i;
            int k = 0;
            while (j != 0) {
                if ((j & 0x01) != 0) {
                    v.add(S[k]);
                }
                k ++;
                j >>= 1;
            }
            uniqueResult.add(v);
        }
        for (ArrayList<Integer> a:uniqueResult) {
            result.add(a);
        }
        return result;
    }
}
