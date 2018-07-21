class Solution {
public:
    string convertToTitle(int n) {
        string s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    	int length = s.length();
    	string result = "";
    	while (n > 0) {
    		n --;
    		result = s[n%length] + result;
    		n /= length;
    	}
    	return result;
    }
};