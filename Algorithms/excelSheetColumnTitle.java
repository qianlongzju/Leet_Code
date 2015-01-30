public class Solution {
    public String convertToTitle(int n) {
        String s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    	int length = s.length();
    	String result = "";
    	while (n > 0) {
    		n --;
    		result = s.charAt(n%length) + result;
    		n /= length;
    	}
    	return result;
    }
}