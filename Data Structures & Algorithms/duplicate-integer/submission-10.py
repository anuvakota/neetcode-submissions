class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset is most efficent
        #make the num list into a set which removes duplicates and if the length not the same yk theres a duplicate
        return len(set(nums)) < len(nums)
        #if the set is less than the original array that means there was a duplicate removed so it returns True bc duplicate
        #O(n)
        
        