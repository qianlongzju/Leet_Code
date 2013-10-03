import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        Arrays.sort(candidates);
        int[] index = new int[target+2];
        index[0] = candidates.length - 1;
        solve(target, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, int[] candidates, int index[], 
            int n, ArrayList<ArrayList<Integer>> result) {
        if (target < 0)
            return ;
        if (target == 0) {
            ArrayList<Integer> v = new ArrayList<Integer>();
            for (int i = n; i >= 1; i--) {
                v.add(candidates[index[i]]);
            }
            result.add(v);
        }
    
        for (int i = index[n]; i >= 0; i--) {
            index[n+1] = i;
            solve(target-candidates[i], candidates, index, n+1, result);
        }
    }
    //public ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
    //    // Start typing your Java solution below
    //    // DO NOT write main() function
    //    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    //    Arrays.sort(candidates);
    //    int[] index = new int[target+2];
    //    index[0] = 0;
    //    solve(target, 0, candidates, index, 0, result);
    //    return result;
    //}
    //
    //void solve(int target, int sum, int[] candidates, int index[], 
    //        int n, ArrayList<ArrayList<Integer>> result) {
    //    if (target < sum)
    //        return ;
    //    if (target == sum) {
    //        ArrayList<Integer> v = new ArrayList<Integer>();
    //        for (int i = 1; i <= n; i++) {
    //            v.add(candidates[index[i]]);
    //        }
    //        result.add(v);
    //    }
    //
    //    for (int i = index[n]; i < candidates.length; i++) {
    //        index[n+1] = i;
    //        solve(target, sum + candidates[i], candidates, index, n+1, result);
    //    }
    //}
}
