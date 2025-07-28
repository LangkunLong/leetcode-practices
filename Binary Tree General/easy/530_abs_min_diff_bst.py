class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # in order traversal, since sorted, we can go to smallest node val first and traverse in incrasing order
        # dfs approach, same as finding min diff in a sorted array, have prev, next nodes
        if not root:
            return 0
        min_diff = [float('inf')]
        prev = [None]

        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            # can only start comparing at second node onwards
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], root.val - prev[0])
            prev[0] = root.val
            
            dfs(root.right)
        
        dfs(root)
        return min_diff[0]
