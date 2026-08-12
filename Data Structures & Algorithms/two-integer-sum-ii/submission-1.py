class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            num_sum = numbers[lp] + numbers[rp]
            if num_sum == target:
                return [1 + lp, 1 + rp]
            elif num_sum > target:
                rp -= 1
            else:
                lp += 1
        
        