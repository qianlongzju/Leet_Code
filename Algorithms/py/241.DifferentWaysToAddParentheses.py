class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        if input.isdigit():
            return [int(input)]
        for i, c in enumerate(input):
            if c not in '+-*':
                continue
            left = self.diffWaysToCompute(input[:i]) 
            right = self.diffWaysToCompute(input[i+1:])
            if c == '+':
                for l in left:
                    for r in right:
                        result.append(l+r)
            elif c == '-':
                for l in left:
                    for r in right:
                        result.append(l-r)
            else:
                for l in left:
                    for r in right:
                        result.append(l*r)
        return result
