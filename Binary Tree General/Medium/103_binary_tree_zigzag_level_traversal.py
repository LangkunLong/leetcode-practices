# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # need to use level-order traversal, easy way to just reverse odd level nodes
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        
        while(queue):
            level = []
            for i in range(len(queue)):
                cur_node = queue.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if len(res) % 2 == 1: # if level is odd, reverse
                level = list(reversed(level))
            res.append(level)
        
        return res
