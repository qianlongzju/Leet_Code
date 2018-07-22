class Solution {
public:
    string simplifyPath(string path) {
        string s;
        stack<string> stk;
        bool begin=false;
        for (int i=0; i < path.size(); i++) {
            if (path[i] == '/') {
                begin = false;
                if (s == "..") {
                    if (stk.empty()) {
                        ;
                    } else {
                        stk.pop();
                    }
                } else if (s == ".") {
                    ;
                } else if (s.size() > 0) {
                    stk.push(s);
                }
                s = "";
            } else if (begin) {
                s += path[i];
            } else {
                begin = true;
                s = path[i];
            }
        }
        if (path.size() > 0 && path[path.size()-1] != '/') {
            if (s == "..") {
                if (stk.empty()) {
                    stk.push(s);
                } else {
                    stk.pop();
                }
            } else if (s == ".") {
                ;
            } else {
                stk.push(s);
            }
        }
        s = ""; 
        while (!stk.empty()) {
            s = stk.top() + "/" + s;
            stk.pop();
        }
        if (s.size() > 1)
            s = s.substr(0, s.size()-1);
        if (s == "..") 
            s = "";
        s = "/" + s;
        return s;
    }
};
