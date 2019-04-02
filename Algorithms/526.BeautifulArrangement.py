class Solution:
    def countArrangement(self, N: int) -> int:
        nums = list(range(1, N+1))
        result, comb = 0, []
        def dfs(nums, i):
            nonlocal result
            if i == N+1:
                result += 1
                return
            for num in nums:
                if num % i == 0 or i % num == 0:
                    comb.append(num)
                    new_nums = nums[:]
                    new_nums.remove(num)
                    dfs(new_nums, i+1)
                    comb.pop()
        dfs(nums, 1)
        return result
