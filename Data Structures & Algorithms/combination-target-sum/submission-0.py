class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(val, seq, start):
            if val == target:
                ans.append(seq[:])
            if val > target:
                return
            for i, n in enumerate(nums):
                if i >= start:
                    seq.append(n)
                    dfs(val + n, seq, i)
                    seq.pop()

        dfs(0, [], 0)
        return ans
            