class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            #print(sorted_s)
            anagrams[sorted_s].append(s)
        
        ans = []
        for a in anagrams:
            ans.append(anagrams[a])
        return ans