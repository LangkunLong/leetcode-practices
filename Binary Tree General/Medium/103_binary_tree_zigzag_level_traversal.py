# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # need to use level-order traversal, alternate between each level 
        # queue can popleft and popright, alternate between popping order but maintain insertion order
        if not root:
            return []
        queue = collections.deque()
        alt = True # so first pop after root is true
        res = []
        
        queue.append(root)
        while(queue):
            num_nodes = len(queue)
            level_trav = []
            for i in range(num_nodes):
                cur_node = None
                if alt:
                    cur_node = queue.popleft()
                else:
                    cur_node = queue.pop()
                if cur_node:
                    level_trav.append(cur_node.val)
                    if cur_node.left:
                        queue.append(cur_node.left)
                    if cur_node.right:
                        queue.append(cur_node.right)
            if not alt:
                level_trav.reverse()
            res.append(level_trav)
            alt = not alt
        
        return res
