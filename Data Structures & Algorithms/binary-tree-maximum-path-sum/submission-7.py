# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo = {}   
        best = [root.val]
        def dp(node):
            if not node:
                return float('-inf')
            
            left = dp(node.left)
            right = dp(node.right)
            left_and_right = left + right + node.val
            left_and_node = left + node.val
            right_and_node = right + node.val

            memo[node] = max([left_and_node, right_and_node, node.val])
            end_path = max([left, right, left_and_right])

            best_path = max(memo[node], end_path)
            #print(node.val, best_path)

            best[0] = max(best[0], best_path)

            return memo[node]
        
        dp(root)
        return best[0]
