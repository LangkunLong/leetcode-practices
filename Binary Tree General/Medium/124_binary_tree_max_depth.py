class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # adjacent node is only between root and left or root and right
        # traverse down the root, if root + root.left/right > maxSum update max Sum
        # at root, calculate max from left subtree, and max from right subtree, then check if needing to connect

        maxSum = [float('-inf')]
        curSum = [0]

        def helper(root, curSum, maxSum):
            if not root:
                return 

            helper(root.left, curSum, maxSum)
            if root.val + curSum[0] > curSum[0]:
                curSum[0] += root.val
                maxSum[0] = max(maxSum[0], curSum[0])
            else:
                curSum[0] = 0 #reset path
            helper(root.right, curSum, maxSum)
        
        helper(root, curSum, maxSum)
        return maxSum[0]