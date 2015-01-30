import java.util.*;
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        HashMap<Integer, Integer> mapping = new HashMap<Integer, Integer>();
        for (int i=0; i < numbers.length; i++) {
            mapping.put(numbers[i], i);
        }
        for (int i = 0; i < numbers.length; i++) {
            int gap = target - numbers[i];
            if (mapping.containsKey(gap) &&
                    mapping.get(gap) != i) {
                result[0] = i + 1;
                result[1] = mapping.get(gap) + 1;
                break;
            }
        }
        return result;
    }
}
