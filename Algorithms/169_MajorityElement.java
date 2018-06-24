public class Solution {
    public int majorityElement(int[] num) {
        int previous = 0;
    	int count = 0;
    	for (int i = 0; i < num.length; i++) {
    		if (count == 0) {
    			previous = num[i];
    			count ++;
    		} else {
    			if (previous == num[i]) {
    				count ++;
    			} else {
    				count --;
    			}
    		}
    	}
    	return previous;  
    }
}