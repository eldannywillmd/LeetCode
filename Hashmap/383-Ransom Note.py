from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for char in ransomNote:
            if char not in count:
                return False
            else:
                count[char] -= 1
                if count[char] < 0:
                    return False
        return True


ransomNote = "a"
magazine = "b"
solution = Solution()
solution.canConstruct(ransomNote, magazine)