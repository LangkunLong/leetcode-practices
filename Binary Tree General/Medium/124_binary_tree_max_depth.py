class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # adjacent node is only between root and left or root and right
        # **** calculated value and return value are different:
        # at root, calculate the value if we can split left and right: root + left + right, this is the max
        # value we can attain at this node, but when we return to the root's parent, we can only pick the max
        # of left subtree or right subtree
        # we can only split once, so at each root, we need to calculate the value if we split, and then when we 
        # return, we only return one subtree
        # left and right might be negative, so we need to compare with 0

        maxSum = [root.val]

        def helper(root, maxSum):
            if not root:
                return 0

            left = helper(root.left, maxSum)
            right = helper(root.right, maxSum)
            # !!! do not want to compute with any negatives, if negative, we do not include it
            left = max(left, 0)
            right = max(right, 0)
            # computer sum with both left and right val
            maxSum[0] = max(maxSum[0], root.val + left + right)
            
            # return sum with maximum subtree, root.val itself can be negative, so need to sanitize when we return
            return max(left, right, 0) + root.val
        
        helper(root, maxSum)
        return maxSum[0]