public class Solution {
        public String multiply(String num1, String num2) {
            int m = num1.length();
            int n = num2.length();
            int[] result = new int[m+n];
            for (int i=0; i < m+n; i++) {
                result[i]= 0;
            }
            int p=0, i=0, j=0;
            for (i=0; i < m; i++) {
                p = 0;
                for (j=0; j < n; j++) {
                    int q = result[i+j] + (num1.charAt(m-1-i)-'0') * (num2.charAt(n-1-j)-'0') + p;
                    result[i+j] = q % 10;
                    p = q / 10;
                }
                if (p != 0) {
                    result[i+j] = p;
                }
            }
            if (p != 0) {
                result[m+n-1] = p;
            }
            String s = "";
            int k = m+n-1;
            for (i=k; i >= 0 && result[i] == 0; i--) {
                ;
            }
            k = i;
            //System.out.println(k);
            for (i=k; i >= 0; i--) {
                s += result[i];
            }
            //System.out.println(s);
            if (s.length() == 0) {
                s += "0";
            }
            return s;
        }
}
