public class Solution {
    public ArrayList<ArrayList<Integer>> generate(int numRows) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (numRows == 0) {
            return result;
        }
        ArrayList<Integer> v = new ArrayList<Integer>();
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
