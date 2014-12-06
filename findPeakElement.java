public class Solution {
    public int findPeakElement(int[] num) {
        return findPeakElement(num, 0, num.length-1);
    }

    private int findPeakElement(int[] num, int start, int end) {
    	if (start == end)
    		return start;
    	int mid = start + (end - start)/2;
    	if ((mid == 0 || num[mid] > num[mid-1]) && (mid+1 > end || num[mid] > num[mid+1]))
    		return mid;
    	else if ((mid == 0 || num[mid] > num[mid-1]) && (mid+1 > end || num[mid] < num[mid+1]))
    		return findPeakElement(num, mid+1, end);
    	else
    		return findPeakElement(num, start, end-1);
    }
}