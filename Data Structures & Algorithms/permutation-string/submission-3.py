class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = {}
        
        l, r = 0, 0
        if len(s1) > len(s2):
            return False

        while r < len(s1):
            count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            r += 1

        while r < len(s2):
            print(l, r)
            if count_s1 == count_s2:
                return True
            else:
                count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
                r += 1

                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    count_s2.pop(s2[l])
                l += 1 
        
        return count_s1 == count_s2



