class Solution {
public:
    bool isNumber(string s) {
        int len = s.size();
        int i = len-1;
        while (i >= 0 && isspace(s[i]))
            i --;
        len = i + 1;
        i = 0;
        while (i < len && isspace(s[i])) 
            i ++;
        if (i < len && (s[i] == '+' || s[i] == '-')) 
            i ++;
        if (i == len)
            return false;
        bool isE = false;
        bool isPoint = false;
        bool hasNum = false;
        while (i < len) {
            if (isdigit(s[i])) {
                hasNum = true;
            } else if (!isE && hasNum && s[i] == 'e') {
                if (i+1 >= len)
                    return false;
                if (s[i+1] == '+' || s[i+1] == '-') {
                    if (i+2 >= len || !isdigit(s[i+2])) {
                        return false;
                    }
                    i += 2;
                }
                else if (isdigit(s[i+1])) {
                    i ++ ;
                }
                else 
                    return false;
                isE = true;
            } else if (!isPoint && !isE && s[i] == '.') {
                if ((i > 0 && isdigit(s[i-1])) || (i < len-1 && isdigit(s[i+1])))
                    isPoint = true;
                else
                    return false;
            } else {
                return false;
            }
            i ++;
        }
        return true;
    }
};
