class Solution:
    def convert(self, s, numRows):

        length = len(s)

        if length == 1 or length <= numRows or numRows == 1:
            return s

        numCols = length // numRows
        step = numRows * 2 - 2
        new_s = []

        for row in range(numRows):
            new_s.append(s[row])
            for col in range(1, numCols + 1):
                if (2 * row) % step != 0 and row + col * step - 2 * row < length:
                    new_s.append(s[row + col * step - 2 * row])
                if row + col * step < length:
                    new_s.append(s[row + col * step])

        return ''.join(new_s)

solution = Solution()
s = "PAYPALISHIRING"
print(solution.convert(s, 2))