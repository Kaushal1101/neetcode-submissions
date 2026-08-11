class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        best_vol = float('-inf')

        while lp < rp:
            volume = (rp - lp) * min(heights[lp], heights[rp])
            best_vol = max(best_vol, volume)
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        
        return best_vol