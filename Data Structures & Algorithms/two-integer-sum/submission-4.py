class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i,n in enumerate(nums):
            complement = target - n
            if complement in indices:
                return [indices[complement],i]
            else:
                indices[n] = i

                        