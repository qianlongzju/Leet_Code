public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> result = new ArrayList<>();
        if (rowIndex == 0) {
            result.add(1);
            return result;
        }
        result.add(1);
        result.add(1);
        for (int i=2; i <= rowIndex; i++) {
            List<Integer> v = new ArrayList<>(result);
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
