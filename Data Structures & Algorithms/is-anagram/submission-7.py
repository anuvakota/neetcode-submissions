class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap 
        if len(s) != len(t):
            return False #base case the length is not equal so u alr know it cant be anagram because not same characters
        countS,countT = {}, {} #create two empty maps
        for i in range(len(s)):
            countS[s[i]] = 1  + countS.get(s[i],0) #if s it not in loop give 0 , if its already in map just increment so its keeping track of how many of each character there are in each set
            #order of the maps dont matter
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #if both maps are same return true     
        

        