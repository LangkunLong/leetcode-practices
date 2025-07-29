class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # can carry out in-order traversal again, if encounter negative value between 2 node values
        # return false
        prev = [None]
        isValid = [True]
        if not root:
            return False
        
        def dfs(cur):
            if not cur:
                return

            dfs(cur.left)
            if prev[0] is not None:
                if cur.val - prev[0] <= 0:
                    isValid[0] = False
            prev[0] = cur.val
            dfs(cur.right)

        dfs(root)
        return isValid[0]
