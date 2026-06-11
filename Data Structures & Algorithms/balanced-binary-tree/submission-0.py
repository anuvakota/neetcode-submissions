# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #check if root node if balancced using DFS on right and left 
    #check left substree and check nodes in that subtree and same for right subtree

    #recursive dfs on every tree O(n) everytime n is number of nodes in trea so O(n^2)

    #instead start from bottom up to be efficent O(n)
    #get height of both subtrees and then compare at parent node after taking the difference u dont need to revist the subnodes again
    #to get the height of root node do 1+max(L,R)
        def dfs(root): 
            if not root:
                return [True,0]
            left,right = dfs(root.left),dfs(root.right)
            balance = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balance, 1+max(left[1],right[1])]
        return dfs(root)[0]