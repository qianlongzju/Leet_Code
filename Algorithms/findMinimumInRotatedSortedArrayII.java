public class Solution {
    public int findMin(int[] num) {
        return findMin(num, 0, num.length-1);
    }
    private int findMin(int[] num, int start, int end) {
        if (start == end)
            return num[start];
        if (num[start] < num[end])
            return num[start];
        int mid = start + (end - start) / 2;
        if (num[start] == num[end])
            return findMin(num, start+1, end);
        if (num[mid] >= num[start])
            return findMin(num, mid+1, end);
        return findMin(num, start, mid);
    }
}
