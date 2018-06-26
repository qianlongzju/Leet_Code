#include "leetcode.h"
class Solution {
public:
    vector<string> fullJustify(vector<string> &words, int L) {
        vs result;    
        int start = 0;
        int length = 0;
        int count = 0;
        string s = "";
        string space = " ";
        int i;
        for (i=0; i < words.size(); ++i) {
            if (length + count + words[i].length() > L) {
                if (count == 1) {
                    s = words[start];
                    while (s.size() < L) {
                        s += space;
                    }
                } else {
                    int numSpace = L - length;
                    s = "";
                    for (int j=start; j < i-1; j++) {
                        s += words[j];
                        for (int k=0; k < (numSpace/(count-1)); k++) {
                            s += space;
                        }
                        if (numSpace%(count-1) != 0) {
                            s += space;
                            numSpace --;
                        }
                    }
                    s += words[i-1];
                }
                result.push_back(s);
                length = words[i].length();
                start = i;
                count = 1;
            } else {
                count ++;
                length += words[i].length();
            }
        } 
        s = words[start];
        for (int j=start+1; j < i; j++) {
            s += space + words[j];
        }
        while (s.length() < L) {
            s += space;
        }
        result.push_back(s);
        return result;
    }
};
int main() {
    Solution s;
    int L = 16;
    vs v;
    v.push_back("This");
    v.push_back("is");
    v.push_back("an");
    v.push_back("example");
    v.push_back("of");
    v.push_back("text");
    v.push_back("justification.");
    v = s.fullJustify(v, L);
    for (int i=0; i < v.size(); ++i) {
        cout << v[i] << " " << v[i].size() << endl;
    }
    cout << endl;
    v.clear();
    v.push_back("Listen");
    v.push_back("to");
    v.push_back("many");
    v.push_back("speak");
    v.push_back("to");
    v.push_back("a");
    v.push_back("few.");
    L = 6;
    v = s.fullJustify(v, L);
    for (int i=0; i < v.size(); ++i) {
        cout << v[i] << " " << v[i].size() << endl;
    }
    cout << endl;
    return 0;
}

