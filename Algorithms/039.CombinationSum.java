public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<>();
        DFS(result, path, candidates, target, 0);
        return result;
    }
    private void DFS(List<List<Integer>> result, List<Integer> path,
            int[] candidates, int target, int level) {
        if (target == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = level; i < candidates.length; i++) {
            if (candidates[i] > target) break;
            path.add(candidates[i]);
            DFS(result, path, candidates, target-candidates[i], i);
            path.remove(path.size()-1);
        }
    }
    /*
    public List<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
        List<ArrayList<Integer>> result = new ArrayList<List<Integer>>();
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
            ArrayList<Integer> v = new ArrayList<>();
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
    */
    /*
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<ArrayList<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(candidates);
        int[] index = new int[target+2];
        index[0] = 0;
        solve(target, 0, candidates, index, 0, result);
        return result;
    }
    
    void solve(int target, int sum, int[] candidates, int index[], 
            int n, List<List<Integer>> result) {
        if (target < sum)
            return ;
        if (target == sum) {
            List<Integer> v = new ArrayList<>();
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
