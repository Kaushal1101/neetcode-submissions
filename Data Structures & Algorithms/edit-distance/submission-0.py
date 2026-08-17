class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # At any point, we can add/replace/delete

        memo = {}

        def dp(p1, p2):
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            elif p1 >= len(word1) and p2 >= len(word2):
                return 0
            
            elif p1 >= len(word1):
                memo[(p1, p2)] = 1 + dp(p1, p2 + 1)
            
            elif p2 >= len(word2):
               memo[(p1, p2)] = 1 + dp(p1 + 1, p2)
            
            elif word1[p1] == word2[p2]:
                memo[(p1, p2)] = dp(p1 + 1, p2 + 1)
            
            else:
                delete = dp(p1 + 1, p2)
                add = dp(p1, p2 + 1)
                replace = dp(p1 + 1, p2 + 1)
                memo[(p1, p2)] = 1 + min([add, delete, replace])
            
            return memo[(p1, p2)]
        
        return dp(0, 0)
            
            