class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = eval(expression)
        result_str = "(" + expression + ")"
        plus = expression.index("+")
        for i in range(plus):
            for j in range(plus+2, len(expression)+1):
                tmp = 1
                if len(expression[:i]) > 0:
                    tmp *= int(expression[:i])
                tmp *= eval(expression[i:j])
                if len(expression[j:]) > 0:
                    tmp *= int(expression[j:])
                if tmp < result:
                    result_str = expression[:i] + "(" + expression[i:j] + ")" + expression[j:]
                    result = tmp
        return result_str
