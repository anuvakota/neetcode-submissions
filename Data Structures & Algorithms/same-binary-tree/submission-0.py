# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True #both are null so they are the same
        if not p or not q or p.val != q.val:
            return False #only one is null so false
        #now the values are teh same so u have to do recursive

        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))

        
        
        