class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
        nums = set()
        for nums in  nums:
            if seen in nums:
                return False
            seen.add(nums)
        return False


        