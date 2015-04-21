import java.util.*;
public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        HashSet<List<Integer>> set_result = new HashSet<List<Integer>>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        DFS(set_result, path, candidates, target, 0, 0);
        for (List<Integer> a: set_result) {
            result.add(a);
        }
        return result;
    }
    private void DFS(HashSet<List<Integer>> result, ArrayList<Integer> path,
            int[] candidates, int target, int level, int sum) {
        if (sum == target) {
            result.add((ArrayList<Integer>)path.clone());
        }
        if (sum > target) return;
        for (int i = level; i < candidates.length; i++) {
            path.add(candidates[i]);
            DFS(result, path, candidates, target, i+1, sum + candidates[i]);
            path.remove(path.size()-1);
        }
    }
    /*
    public ArrayList<ArrayList<Integer>> combinationSum2(int[] candidates, int target) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> temp = new HashSet<ArrayList<Integer>>();
        Arrays.sort(candidates);
        int[] index = new int[target+2];
        index[0] = candidates.length;
        solve(target, candidates, index, 0, temp);
        for (ArrayList<Integer> a:temp) {
            result.add(a);
        }
        return result;
    }
    
    void solve(int target, int[] candidates, int index[], 
            int n, HashSet<ArrayList<Integer>> result) {
        if (target < 0)
            return ;
        if (target == 0) {
            ArrayList<Integer> v = new ArrayList<Integer>();
            for (int i = n; i >= 1; i--) {
                v.add(candidates[index[i]]);
            }
            result.add(v);
        }
    
        for (int i = index[n]-1; i >= 0; i--) {
            index[n+1] = i;
            solve(target-candidates[i], candidates, index, n+1, result);
        }
    }
    */
    /*
    public ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        Arrays.sort(candidates);
        int[] index = new int[target+2];
        index[0] = 0;
        solve(target, 0, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, int sum, int[] candidates, int index[], 
            int n, ArrayList<ArrayList<Integer>> result) {
        if (target < sum)
            return ;
        if (target == sum) {
            ArrayList<Integer> v = new ArrayList<Integer>();
            for (int i = 1; i <= n; i++) {
                v.add(candidates[index[i]]);
            }
            result.add(v);
        }
    
        for (int i = index[n]; i < candidates.length; i++) {
            index[n+1] = i;
            solve(target, sum + candidates[i], candidates, index, n+1, result);
        }
    }
    */
}
