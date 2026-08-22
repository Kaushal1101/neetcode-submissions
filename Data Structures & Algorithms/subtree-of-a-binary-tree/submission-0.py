# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, duplicate):
            if not node and not duplicate:
                return True
            
            if not node or not duplicate:
                return False
            
            if node.val != duplicate.val:
                return False
            
            return dfs(node.left, duplicate.left) and dfs(node.right, duplicate.right)
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        ans = False
        if root.val == subRoot.val:
            ans = dfs(root, subRoot)
        
        return ans or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
