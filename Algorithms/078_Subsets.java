import java.util.*;
public class Solution {
    public List<List<Integer>> subsets(int[] S) {
        Arrays.sort(S);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> current = new ArrayList<Integer>();
        subsetsHelper(result, current, S, 0);
        return result;
    }
    private void subsetsHelper(List<List<Integer>> result, List<Integer> current, int[] S, int pos) {
        result.add((List)((ArrayList)current).clone());
        for (int i = pos; i < S.length; i++) {
            current.add(S[i]);
            subsetsHelper(result, current, S, i+1);
            current.remove(current.size()-1);
        }
    }
    /*
    public ArrayList<ArrayList<Integer>> subsets(int[] S) {
        Arrays.sort(S);        
        int n = S.length;
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
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
            result.add(v);
        }
        return result;
    }
    */
}
