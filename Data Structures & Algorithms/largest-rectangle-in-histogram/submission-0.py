class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best_area = 0
        length = len(heights)

        for i, h in enumerate(heights):
            prev_index = i
            while stack and h <= stack[-1][1]:
                prev_bar = stack.pop()
                prev_index, prev_height = prev_bar[0], prev_bar[1]
                best_area = max(best_area, (i - prev_index) * prev_height)

            stack.append([prev_index, h])
    
        
        while stack:
            prev_bar = stack.pop()
            prev_index, prev_height = prev_bar[0], prev_bar[1]
            best_area = max(best_area, (length - prev_index) * prev_height)
            print(best_area)
        
        return best_area
            
            
        
