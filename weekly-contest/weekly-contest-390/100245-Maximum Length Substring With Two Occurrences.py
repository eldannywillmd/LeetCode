class Solution:
    def maximumLengthSubstring(self, s):
        chars_in_string = {}
        chars = 'abcdefghijklmnopqrstuvwxyz'

        # create a dictionary with the chars in s and start value with 0
        for char in chars:
            if char in s:
                chars_in_string[char] = 0

        count = 0
        max_count = 0

        # go through s and update the dictionary with the counting
        for i in range(len(s)):
            count += 1
            chars_in_string[s[i]] += 1
            if chars_in_string[s[i]] == 3:
                count = 0
                # clean chars_in_string
                for key in chars_in_string.keys():
                    chars_in_string[key] = 0
                # go back and check the beginning of new substring
                for j in reversed(range(i + 1)):
                    count += 1
                    chars_in_string[s[j]] += 1
                    if chars_in_string[s[j]] == 3:
                        count -= 1
                        chars_in_string[s[j]] = 2
                        break
            if count > max_count:
                max_count = count

        return max_count


ss = ["bbachascbcbsjcsbefeijbjcsdkc",
"bcbbbccas",
"bcbbbccasrba",
"aaaa",
"bb",
"acedc",
"aaaaaaaaaaaaaa",
"bbbaaaaba",
"acbacbacbacbacbacbacbacb"]

solution = Solution()
for s in ss:
    print(solution.maximumLengthSubstring(s))