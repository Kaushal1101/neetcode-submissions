class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        stack = [[temperatures[0], 0]]

        for i in range(1, len(temperatures)):
            t = temperatures[i]
            if (stack and stack[-1][0] < t):
                while stack and stack[-1][0] < t:
                    old_val = stack.pop()
                    ans[old_val[1]] = i - old_val[1]

            stack.append([t, i])
        
        return ans

            