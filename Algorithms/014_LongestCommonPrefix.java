public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        int i;
        for (i=0; i < strs[0].length(); i++) {
            int j;
            for (j=1; j < strs.length; j++) {
                if (i < strs[j].length() && strs[j].charAt(i) == strs[0].charAt(i)) {
                    ;
                }
                else {
                    break;
                }
            }
            if (j != strs.length) {
                break;
            }
        }
        return strs[0].substring(0, i);
    }
}
