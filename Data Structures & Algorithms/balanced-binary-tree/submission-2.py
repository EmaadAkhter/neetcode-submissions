# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0
            
            h_l=height(root.left)
            if h_l == -1:
                return -1
            
            h_r=height(root.right)
            if h_r == -1:
                return -1
            
            if abs(h_l-h_r)>1:
                return -1
            
            return max(h_l,h_r)+1
        
        return height(root) !=-1

        