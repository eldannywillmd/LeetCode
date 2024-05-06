class Solution:
    def groupAnagrams(self, strs):
        strs_map = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in strs_map:
                strs_map[sorted_s].append(s)
            else:
                strs_map[sorted_s] = [s]

        return list(strs_map.values())

strs = ["ivy","hop","dug","chi","tub","man","yak","pub","son","ohm","gut","hem","pub","gad","hew","bit","arm","vat","sop","nan","dot","fdr","tad","big","her","yea","sis"]
solution = Solution()
print(solution.groupAnagrams(strs))