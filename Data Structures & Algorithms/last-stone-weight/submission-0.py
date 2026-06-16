class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort() #sorts the stones
            cur = stones.pop() - stones.pop() #pops the last 2 and subtracts
            if cur: #if it has a value not 0 then append the difference
                stones.append(cur)
        return stones[0] if stones else 0 #if not that means smash so return index 0 weight or 0 if none
