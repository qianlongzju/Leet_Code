public class Solution {
    public ArrayList<String> restoreIpAddresses(String s) {
        int n = s.length();
        ArrayList<String> v = new ArrayList<String>();
        String temp = "";
        for (int i=1; i <= 3 && i < n; i++) {
            int a = Integer.parseInt(s.substring(0, i));
            if (a > 255) {
                continue;
            }
            for (int j=i+1; j <= i+3 && j < n; j++) {
                int b = Integer.parseInt(s.substring(i, j));
                if (b > 255) {
                    continue;
                }
                for (int k=j+1; k <= j+3 && k < n; k++) {
                    int c = Integer.parseInt(s.substring(j, k)); 
                    if (n-k >3) {
                        continue;
                    }
                    int d = Integer.parseInt(s.substring(k, n)); 
                    if (c > 255 || d > 255) {
                        continue;
                    }
                    temp = a + "." + b + "." + c + "." + d;
                    if (temp.length() == n + 3) {
                        v.add(temp);
                    }
                }
            }
        }
        return v;
    }
}
