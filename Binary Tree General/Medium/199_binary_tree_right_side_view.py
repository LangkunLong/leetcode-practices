# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # for each level of nodes, only want to return the right child, only return left if that level does not 
        # have right node
        # only add to solution when we find a lower depth
        
        res = []
        all_depth = [0]
        cur_depth = [0]
        def helper(root):
            if not root:
                return None
            cur_depth[0] += 1
            if cur_depth[0] > all_depth[0]:
                res.append(root.val)
                all_depth[0] = cur_depth[0]
            
            helper(root.right) # when we return from right subtree, we should have most (if not all) solution nodes
            helper(root.left)
            cur_depth[0] -= 1 # go back to root, decrease the current traversal level
        
        helper(root)
        return res

            
        
