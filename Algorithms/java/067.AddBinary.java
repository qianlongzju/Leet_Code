public class Solution {
    public String addBinary(String a, String b) {
        int m = a.length();
        int n = b.length();
        int p = 0, i;
        String s = "";
        for (i=0; i < m && i < n; i++) {
            int q = a.charAt(m-1-i) - '0' + b.charAt(n-1-i) - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s = '1' + s;
            }
            else {
                s = '0' + s;
            }
        }
        for (; i < m; i++) {
            int q = a.charAt(m-1-i) - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s = '1' + s;
            }
            else {
                s = '0' + s;
            }
        }
        for (; i < n; i++) {
            int q = b.charAt(n-1-i) - '0' + p;
            p = q / 2;
            if (q%2 == 1) {
                s = '1' + s;
            }
            else {
                s = '0' + s;
            }
        }
        if (p != 0) {
            s = '1' + s;
        }
        return s;
    }
}
