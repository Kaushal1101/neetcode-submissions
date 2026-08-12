class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            val = nums[i]
            lp, rp = i + 1, length - 1
            while lp < rp:
                pointer_sum = nums[lp] + nums[rp] + val
                if pointer_sum == 0:
                    ans.append([val, nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    while lp < length and nums[lp] == nums[lp - 1]:
                        lp += 1
                    while rp > 0 and nums[rp] == nums[rp + 1]:
                        rp -= 1
                elif pointer_sum > 0:
                    rp -= 1
                else:
                    lp += 1
        
        return ans