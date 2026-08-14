class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        length = len(s)

        def dp(index):
            if index >= length:
                return True
            if index in memo:
                return memo[index]
            
            for word in wordDict:
                if word == s[index: index + len(word)] and dp(index + len(word)):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False
        
        return dp(0)