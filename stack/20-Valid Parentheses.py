class Solution:
    def isValid(self, s):
        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                if stack:
                    close = stack.pop()
                    if char != brackets[close]:
                        return False
                else:
                    return False
        return len(stack) == 0

s = "((({{()))"
solution = Solution()
print(solution.isValid(s))