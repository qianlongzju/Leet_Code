class Solution {
public:
    int compareVersion(string version1, string version2) {
        vector<string> tokens1 = split(version1, '.');
        vector<string> tokens2 = split(version2, '.');

        int length = 0;
        if (tokens1.size() > tokens2.size())
            length = tokens1.size();
        else
            length = tokens2.size();
        for (int i = 0; i < length; i++) {
            int a = 0, b = 0;
            if (i < tokens1.size())
                a = atoi(tokens1[i]);
            if (i < tokens2.size())
                b = atoi(tokens2[i]);
            if (a > b)
                return 1;
            if (a < b)
                return -1;
        }
        return 0;
    }
 private:
    vector<string>& split(const string& s, char delim, vector<string>& elems) {
        stringstream ss(s);
        string item;
        while (getline(ss, item, delim)) {
            elems.push_back(item);
        }
        return elems;
    }

    vector<string> split(const string& s, char delim) {
        vector<string> elems;
        split(s, delim, elems);
        return elems;
    }
};
