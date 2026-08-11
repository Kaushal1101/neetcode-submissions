class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, t):
            if index == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0
            if (index, t) in memo:
                return memo[(index, t)]

            memo[(index, t)] = dp(index + 1, t - nums[index]) + dp(index + 1, t + nums[index])
            return memo[(index, t)]

        return dp(0, target)