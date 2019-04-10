class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;    
        int start = 0;
        int length = 0;
        int count = 0;
        string s = "";
        string space = " ";
        int i;
        for (i=0; i < words.size(); ++i) {
            if (length + count + words[i].length() > maxWidth) {
                if (count == 1) {
                    s = words[start];
                    while (s.size() < maxWidth) {
                        s += space;
                    }
                } else {
                    int numSpace = maxWidth - length;
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
        for (int j=start+1; j < words.size(); j++) {
            s += space + words[j];
        }
        while (s.length() < maxWidth) {
            s += space;
        }
        result.push_back(s);
        return result;
    }
};
