class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        best_seq = 0
        seq = 1
        for num in nums:
            if num - 1 in num_set:
                continue
            else:
                while num + 1 in num_set:
                    seq += 1
                    num += 1
                best_seq = max(best_seq, seq)
                seq = 1
        
        return best_seq