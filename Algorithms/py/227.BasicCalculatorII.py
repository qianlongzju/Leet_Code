class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        flag = False
        for i in range(len(s)):
            if s[i].isdigit():
                if not flag:
                    j = i
                flag = True
            else:
                if flag:
                    nums.append(s[j:i])
                flag = False
        if flag:
            nums.append(s[j:])
        operators = [c for c in s if c in "+-*/"]
        s = [int(nums[0])]
        i = 0
        while i < len(operators):
            operator = operators[i]
            n = int(nums[i+1])
            if operator == '+':
                s.append(n)
            elif operator == '-':
                s.append(-n)
            elif operator == '*':
                p = s.pop()
                s.append(p * n)
            else:
                p = s.pop()
                flag = 1
                if p < 0:
                    flag = -1
                    p = -p
                s.append(flag * (p/n))
            i += 1
        return sum(s)
