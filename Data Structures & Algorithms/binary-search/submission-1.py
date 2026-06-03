class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            aveg = l + (r- l)//2
            if nums[aveg] < target:
                l = aveg + 1
            elif nums[aveg] > target:
                r = aveg - 1
            else:
                return aveg
        return -1
