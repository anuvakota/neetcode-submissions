class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n #creates a list full of zeros to hold result
        pref = [0] * n # hold values before
        post = [0] * n #holds values after

        pref[0] = post[n - 1] = 1 #sets the prefix for first val and last post for last to 1 since there is nothing there

        for i in range(1,n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        for i in range(n):
            result[i] = pref[i] * post[i]
        return result

        