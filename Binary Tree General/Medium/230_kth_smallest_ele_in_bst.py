class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use same traversal method, using in-order go to leftmost node first, then traverse back
        if not root:
            return 0
        
        cur_pos = [0]
        res = [0]
        
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            if cur_pos[0] == k - 1:
                res[0] = root.val
            # increase cur position
            cur_pos[0] += 1
            
            dfs(root.right)
        
        dfs(root)
        return res[0]
