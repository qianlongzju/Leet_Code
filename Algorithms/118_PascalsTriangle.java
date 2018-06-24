public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (numRows == 0) {
            return result;
        }
        List<Integer> v = new ArrayList<Integer>();
        v.add(1);
        result.add(v);
        for (int i=2; i <= numRows; i++) {
            ArrayList<Integer> v1 = new ArrayList<Integer>();
            v1.add(1);
            for (int j=1; j < i-1; j++) {
                v1.add(result.get(i-2).get(j-1) + result.get(i-2).get(j));
            }
            v1.add(1);
            result.add(v1);
        }
        return result;
    }
}
