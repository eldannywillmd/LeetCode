from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            value = 1
            for char in s:
                value *= ord(char)
            if value not in anagrams.keys():
                anagrams[value] = [s]
            else:
                anagrams[value].append(s)

        return list(anagrams.values())

    def groupAnagrams2(self, strs):
        anagrams = {}
        for s in strs:
            new = self.get_unique_hash(s)
            if new in anagrams:
                anagrams[new].append(s)
            else:
                anagrams[new] = [s]

        return anagrams

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams2(strs))