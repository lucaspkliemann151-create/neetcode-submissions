class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                current_num = i
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1
                if current_streak >= longest:
                    longest = current_streak            
        return longest