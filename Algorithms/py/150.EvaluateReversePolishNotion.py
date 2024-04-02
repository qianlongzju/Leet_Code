class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(b + a)
                elif c == '-':
                    stack.append(b - a)
                elif c == '*':
                    stack.append(b * a)
                elif c == '/':
                    stack.append((abs(b) // abs(a)) * (1 if a * b > 0 else -1))
            else:
                stack.append(int(c))
        return stack.pop()