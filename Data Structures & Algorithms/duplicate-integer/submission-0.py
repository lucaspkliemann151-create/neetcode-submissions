class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set(nums)
        return not(len(setnums) == len(nums))