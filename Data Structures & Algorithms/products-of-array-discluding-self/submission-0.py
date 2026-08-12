class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = [1]
        for i in range(1, len(nums)):
            prefix_left.append(nums[i - 1] * prefix_left[i - 1])
        
        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix_left[i] *= right_prod
            right_prod *= nums[i]
        
        return prefix_left