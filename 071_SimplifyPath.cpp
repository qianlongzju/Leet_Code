#include "leetcode.h"
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
                        //stk.push(s);
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
        //cout << s << endl;
        if (s.size() > 1)
            s = s.substr(0, s.size()-1);
            //s.erase(s.end()-1, s.end());
        if (s == "..") 
            s = "";
        s = "/" + s;
        return s;
    }
};
int main() {
    Solution s;
    //cout << s.simplifyPath("/home/") << endl;
    //cout << s.simplifyPath("/a/./b/../../c/") << endl;
    //cout << s.simplifyPath("/foo//bar/") << endl;
    //cout << s.simplifyPath("/../") << endl;
    cout << s.simplifyPath("/") << endl;
    cout << s.simplifyPath("////") << endl;
    cout << s.simplifyPath("/..") << endl;
    cout << s.simplifyPath("/.hidden") << endl;
    cout << s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") << endl;

    return 0;
}

