class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        max_bananas = max(piles)
        
        def check_rate(r, h):
            for p in piles:
                h -= math.ceil(p / r)
                if h < 0:
                    return False
            return True

        l, r = 1, max_bananas
        best = 0
        while l < r:
            mid = (l + r) // 2
            if check_rate(mid, h):
                r = mid
            else:
                l = mid + 1
        
        return l
