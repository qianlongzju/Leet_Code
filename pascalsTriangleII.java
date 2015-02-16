public class Solution {
    public ArrayList<Integer> getRow(int rowIndex) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (rowIndex == 0) {
            result.add(1);
            return result;
        }
        result.add(1);
        result.add(1);
        for (int i=2; i <= rowIndex; i++) {
            ArrayList<Integer> v = new ArrayList<Integer>(result);
            result.clear();
            result.add(1);
            for (int j=1; j < i; j++) {
                result.add(v.get(j-1) + v.get(j));
            }
            result.add(1);
        }
        return result;

    }
}
