# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #result global variable stores the diameter and updates the largest left+right
        #create a function to return just the height first
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right) #recursively calls the functions
            self.res = max(self.res, left+right)
            return 1+ max(left,right)
        dfs(root)
        return self.res
        
        