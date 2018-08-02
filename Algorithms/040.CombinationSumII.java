public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
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
            if (i != level && candidates[i] == candidates[i-1]) continue;
            if (candidates[i] > target) break;
            path.add(candidates[i]);
            DFS(result, path, candidates, target-candidates[i], i+1);
            path.remove(path.size()-1);
        }
    }
    /*
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        Set<List<Integer>> set_result = new HashSet<List<Integer>>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<>();
        DFS(set_result, path, candidates, target, 0, 0);
        for (List<Integer> a: set_result) {
            result.add(a);
        }
        return result;
    }
    private void DFS(Set<List<Integer>> result, List<Integer> path,
            int[] candidates, int target, int level, int sum) {
        if (sum == target) {
            result.add(new ArrayList<>(path));
        }
        if (sum > target) return;
        for (int i = level; i < candidates.length; i++) {
            path.add(candidates[i]);
            DFS(result, path, candidates, target, i+1, sum + candidates[i]);
            path.remove(path.size()-1);
        }
    }
    */
    /*
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> temp = new HashSet<List<Integer>>();
        Arrays.sort(candidates);
        int[] index = new int[target+2];
        index[0] = candidates.length;
        solve(target, candidates, index, 0, temp);
        for (List<Integer> a:temp) {
            result.add(a);
        }
        return result;
    }
    
    void solve(int target, int[] candidates, int index[], 
            int n, Set<List<Integer>> result) {
        if (target < 0)
            return ;
        if (target == 0) {
            List<Integer> v = new ArrayList<>();
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
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
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
