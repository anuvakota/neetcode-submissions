class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1 #set two pointers one at beginning and one and the end of array
        while l < r: #make sures the pointers dont overlap
            curSum = numbers[l] + numbers[r]
            if curSum > target: #sum is greater than target
                r -= 1 # you want smaller values so move right pointer lower
            elif curSum < target: #want larget value so increment more so move left
                l += 1
            else:
                return [l + 1, r+ 1] 
        return []

            
        