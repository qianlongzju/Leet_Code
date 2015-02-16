import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        combine(n, k, 1, path, result);
        return result;
    }
    void combine(int n, int k, int min, ArrayList<Integer> path, 
            ArrayList<ArrayList<Integer>> result) {
        ArrayList<Integer> clone_path = (ArrayList<Integer>)path.clone();
        if (clone_path.size() == k) {
            result.add(clone_path);
            return;
        }
        if (min > n) {
            return;
        }
        combine(n, k, min+1, clone_path, result);
        clone_path.add(min);
        combine(n, k, min+1, clone_path, result);
    }
    //public ArrayList<ArrayList<Integer>> combine(int n, int k) {
    //    
    //    ArrayList<ArrayList<Integer> > result = new ArrayList<ArrayList<Integer>>();
    //    for (int i=0; i < Math.pow(2, n); i++) {
    //        ArrayList<Integer> v = new ArrayList<Integer>();
    //        int j = i;
    //        int p = 1;
    //        int q = 0;
    //        while (j != 0) {
    //            if ((j & 0x01) != 0) {
    //                v.add(p);
    //                q ++;
    //            }
    //            p ++;
    //            j >>= 1;
    //        }
    //        if (k == q) {
    //            result.add(v);
    //        }
    //    }
    //    return result;
    //}
}
