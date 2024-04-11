from collections import defaultdict

import numpy
class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        ans = []
        for s in strs:
            value = 0
            for char in s:
                value += ord(char) # get numeric value of the char ?? How to get value of char?
            # all anagrams will have the same (length, value) pair -> add to anagrams
            if len(s) * value not in anagrams.keys():
                anagrams[len(s)*value] = s
            else:
                anagrams[len(s) * value].add(s)

        for anagram in anagrams:
            ans.append([anagrams[anagram]])
        print(ans)
        return ans

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
solution.groupAnagrams(strs)