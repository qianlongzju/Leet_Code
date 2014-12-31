class Solution {
public:
    int compareVersion(string version1, string version2) {
    	std::vector<std::string> tokens1 = split(version1, '.');
    	std::vector<std::string> tokens2 = split(version2, '.');

    	int length = 0;
    	if (tokens1.size() > tokens2.size())
    		length = tokens1.size();
    	else
    		length = tokens2.size();
    	for (int i = 0; i < length; i++) {
    	    int a = 0, b=0;
    		if (i < tokens1.size())
    			a = tokens1[i];
    		if (i < tokens2.size())
    			b = tokens2[i];
    		if (a > b)
    			return 1;
    		if (a < b)
    			return -1;
    	}
    	return 0;
    }
 private:
 	std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    	std::stringstream ss(s);
    	std::string item;
    	while (std::getline(ss, item, delim)) {
        	elems.push_back(item);
    	}
    	return elems;
	}

	std::vector<std::string> split(const std::string &s, char delim) {
    	std::vector<std::string> elems;
    	split(s, delim, elems);
    	return elems;
	}
};