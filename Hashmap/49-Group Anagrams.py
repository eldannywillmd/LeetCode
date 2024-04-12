
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
            value = 1
            for char in s:
                value *= ord(char)
            if value not in anagrams.keys():
                anagrams[value] = [s]
            else:
                anagrams[value].append(s)

        return list(anagrams.values())

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams2(strs))