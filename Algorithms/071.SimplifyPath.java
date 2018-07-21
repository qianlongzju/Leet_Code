public class Solution {
    public String simplifyPath(String path) {
            String s = "";
            Stack<String> stk = new Stack<String>();
            boolean begin=false;
            for (int i=0; i < path.length(); i++) {
                if (path.charAt(i) == '/') {
                    begin = false;
                    if (s.equals("..")) {
                        if (stk.isEmpty()) {
                            ;
                        } else {
                            stk.pop();
                        }
                    } else if (s.equals(".")) {
                        ;
                    } else if (s.length() > 0) {
                        stk.push(s);
                    }
                    s = "";
                } else if (begin) {
                    s += path.charAt(i);
                } else {
                    begin = true;
                    s = "" + path.charAt(i);
                }
            }
            if (path.length() > 0 && path.charAt(path.length()-1) != '/') {
                if (s.equals("..")) {
                    if (stk.isEmpty()) {
                        ;
                    } else {
                        stk.pop();
                    }
                } else if (s.equals(".")) {
                    ;
                } else {
                    stk.push(s);
                }
            }
            s = ""; 
            while (!stk.isEmpty()) {
                s = stk.pop() + "/" + s;
            }
            if (s.length() > 1)
                s = s.substring(0, s.length()-1);
            if (s.equals(".."))
                s = "";
            s = "/" + s;
            return s;
    }
}
