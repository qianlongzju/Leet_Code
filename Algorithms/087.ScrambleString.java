public class Solution {
    public boolean isScramble(String s1, String s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        if (l1 != l2)
            return false;
        if (l1 == 0)
            return true;
        if (l1 == 1) 
            return s1.charAt(0) == s2.charAt(0);
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
        for (int i=0; i < l1; i++)
            if (c1[i] != c2[i])
                return false;
        for (int i=1; i < l1; i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i);
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i);
            if (isScramble(s11, s21) && isScramble(s12, s22))
                return true;
            String s23 = s2.substring(0, l1-i);
            String s24 = s2.substring(l1-i);
            if (isScramble(s11, s24) && isScramble(s12, s23))
                return true;
        }
        return false;
    }
}
