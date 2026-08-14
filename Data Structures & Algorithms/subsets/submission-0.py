class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(index, seq):
            if index == len(nums):
                ans.append(seq[:])
                return
            
            dfs(index + 1, seq)
            seq.append(nums[index])
            dfs(index + 1, seq)
            seq.pop()
        
        dfs(0, [])
        return ans