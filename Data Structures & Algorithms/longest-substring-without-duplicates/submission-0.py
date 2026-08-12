class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_seen = set()
        longest = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in chars_seen:
                longest = max(longest, r - l)
                while s[r] in chars_seen:
                    chars_seen.remove(s[l])
                    l += 1
                
            chars_seen.add(s[r])
            r += 1
        
        # do something else
        return max(longest, r - l)