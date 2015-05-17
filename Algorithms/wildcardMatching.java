public class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int mm = 0;
        int n = p.length();
        int nn = 0;
        boolean star = false;
        int i;
        for (i=0; i+mm < m; i++) {
            if (i+nn >= n) {
                if (star) {
                    mm ++;
                    i = -1;
                    continue;
                } else {
                    return false;
                }
            }
            switch(p.charAt(i+nn)) {
                case '?':
                    break;
                case '*':
                    star = true;
                    nn += i+1;
                    mm += i;
                    i = 0;
                    while (i+nn < n && p.charAt(i+nn) == '*') {
                        i ++;
                    }
                    if (i+nn == n) 
                        return true;
                    i = -1;
                    break;
                default:
                    if (s.charAt(i+mm) != p.charAt(i+nn)) {
                        if (star) {
                            mm ++;
                            i = -1;
                        } else {
                            return false;
                        }
                    }
                    break;
            }
        }
        while (i+nn < n && p.charAt(i+nn) == '*') {
            i ++;
        }
        return i+nn == n;
    }
}
