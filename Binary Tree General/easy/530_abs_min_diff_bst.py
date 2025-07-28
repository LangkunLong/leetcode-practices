# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # find minimum, given a bst, sorted
        # min difference is (root.right - root), (root - root.left), then traverse left
        # any traversal works, doing in order
        if not root:
            return 0
        min_diff = [float('inf')] # initialize
        def helper(root):
            if not root:
                return 
            if root.left:
                min_diff[0] = min(min_diff[0], root.val - root.left.val)
                helper(root.left)
            if root.right:
                min_diff[0] = min(min_diff[0], root.right.val - root.val )
                helper(root.right)
        
        helper(root)
        return min_diff[0]
