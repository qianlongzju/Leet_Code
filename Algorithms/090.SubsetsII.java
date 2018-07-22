public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> current = new ArrayList<>();
        subsetsHelper(result, current, num, 0);
        return result;
    }
    private void subsetsHelper(List<List<Integer>> result, List<Integer> current, int[] S, int pos) {
        result.add(new ArrayList<>(current));
        for (int i = pos; i < S.length; i++) {
            if (i != pos && S[i] == S[i-1]) continue;
            current.add(S[i]);
            subsetsHelper(result, current, S, i+1);
            current.remove(current.size()-1);
        }
    }
    /*
    public List<List<Integer>> subsetsWithDup(int[] S) {
        Arrays.sort(S);        
        int n = S.length;
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Set<List<Integer>> uniqueResult = new HashSet<List<Integer>>();
        for (int i=0; i < Math.pow(2, n); i++) {
            List<Integer> v = new ArrayList<>();
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
        for (List<Integer> a:uniqueResult) {
            result.add(a);
        }
        return result;
    }
    */
}
