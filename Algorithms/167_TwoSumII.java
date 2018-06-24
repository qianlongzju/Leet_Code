class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        for (int i=0, j=numbers.length-1; i < j;) {
            if (numbers[i] + numbers[j] < target) i++;
            if (numbers[i] + numbers[j] > target) j--;
            if (numbers[i] + numbers[j] == target) {
                result[0] = i+1;
                result[1] = j+1;
                break;
            }
        }
        return result;
    }
}
