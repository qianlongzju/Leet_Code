public class Solution {
    public int compareVersion(String version1, String version2) {
        String[] tokens1 = version1.split("\\.");
    	String[] tokens2 = version2.split("\\.");
    	int length = 0;
    	if (tokens1.length > tokens2.length)
    		length = tokens1.length;
    	else
    		length = tokens2.length;
    	for (int i = 0; i < length; i++) {
    	    int a = 0, b=0;
    		if (i < tokens1.length)
    			a = Integer.parseInt(tokens1[i]);
    		if (i < tokens2.length)
    			b = Integer.parseInt(tokens2[i]);
    		if (a > b)
    			return 1;
    		if (a < b)
    			return -1;
    	}
    	return 0;
    }
    public static void main(String[] args) {
    	Solution s = new Solution();
    	System.out.println(s.compareVersion("1.1", "0.1"));
    }
}