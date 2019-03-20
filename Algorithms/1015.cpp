class Solution {
public:
    void int2vector(int num, vector<int>& vec) {
    while (num > 0) {
        int remain = num % 10;
        vec.insert(vec.begin(), remain);
        num /= 10;
    }
    // for (const auto& i : vec) {
    // 	cout << i << " ";
    // }
    // cout << "\n";
}

int vector2int(const vector<int>& vec) {
	int result = 0;
	for (const auto & i : vec) {
		result = result * 10 + i;
	}
	return result;
}

int count(int used_digits, int remain_step) {
	if (remain_step < 0) {
		return 1;
	}
	int result = 1;
	for (int i = 0; i <= remain_step; ++i) {
		result *= (10 - used_digits - i);
	}
	return result;
}

bool unique_digit(int num, int digit) {
	if (num == 0 && digit == 0) {
		return true;
	}
	while (num > 0) {
		if (num % 10 == digit) {
			return false;
		}
		num /= 10;
	}
	return true;
}

int num_len(int num) {
	int len = 0;
	while (num > 0) {
		num /= 10;
		len++;
	}
	return len;
}

int dfs(int prefix, int index, const vector<int>& nums) {
	// cout << "dfs(" << prefix << "," << index << ")\n";
	if (index >= nums.size()) {
		return 1;
	}

	vector<int> prefix_nums(nums.begin(), nums.begin() + index);
	int num = vector2int(prefix_nums);

	// cout << num << "\n";
	if (prefix > num) {
		return 0;
	}

	int start = 0;
	int end = 9;
	int result = 0;

	if (prefix < num && prefix != 0) {
		// cout << "count(" << index << "," << nums.size()-1-index << ")\n";
		return count(num_len(prefix), nums.size()-1-index);
	}

	if (prefix == num) {
		end = nums[index];
	}

	for (int i = start; i <= end; ++i) {
		if (unique_digit(prefix, i)) {
			result += dfs(i + prefix * 10, index + 1, nums);
		}
	}

	return result;
}

int unique_count(const int num) {
	vector<int> nums;
    int2vector(num, nums);
	return dfs(0, 0, nums);
}

int numDupDigitsAtMostN(const int num) {
	return num - (unique_count(num) - 1);
}

};


