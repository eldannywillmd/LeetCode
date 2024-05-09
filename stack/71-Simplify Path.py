class Solution:
    def simplifyPath(self, path):
        stack = ''
        length = len(path)

        for index, char in enumerate(path):
            if stack:
                if char == '/' and stack[-1] == '/':
                    continue
                elif char == '/' and stack[-2:] == '/.':
                    stack = stack[:-2]
                    stack += char
                elif (char == '/' and stack[-3:] == '/..') or (index == length - 1 and char == '.' and stack[-2:] == '/.'):
                    if len(stack) == 3:
                        stack = '/'
                    else:
                        stack = stack[:-3]
                    if stack:
                        if stack[-2:] == '/.':
                            stack = stack[:-2]
                        while stack[-1] != '/':
                            stack = stack[:-1]
                            if not stack:
                                stack = '/'
                                break
                else:
                    stack += char

                if stack and stack[0] != '/':
                    stack = '/' + stack
            else:
                stack += char

        if stack:
            if len(stack) > 1 and stack[-2:] == '/.':
                stack = stack[:-1]
            if stack == '/..':
                stack = '/'
            if len(stack) > 1 and stack[-1] == '/':
                stack = stack[:-1]
            return stack
        else:
            return '/'

    # solution form leetcode. Simply beautiful.
    def simplifyPath2(self, path: str) -> str:
        stack = []
        for ch in path.split('/'):
            # drop double char
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch == '.' or not ch:
                continue
            else:
                stack.append(ch)
        final_str = "/" + "/".join(stack)
        return final_str

path = "/home/of/foo/../../bar/../../is/./here/."
solution = Solution()
print(solution.simplifyPath2(path))