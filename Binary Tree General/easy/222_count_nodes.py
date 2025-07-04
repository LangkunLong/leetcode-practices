class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]

        def helper(root):
            if not root:
                return 
            helper(root.left)
            count[0] += 1
            helper(root.right)
        
        helper(root)
        return count[0]
