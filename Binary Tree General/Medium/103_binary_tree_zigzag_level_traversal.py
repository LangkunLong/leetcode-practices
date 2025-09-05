# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # try solving with correct traversal order
        # in tree problems, keep in in mind:
        # traversal order: BFS, maintain the structure of the tree, make sure traversing level by level
        # output order: in this question zigzag, left to right then right to left
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []
        zigzag = True
        
        while(queue):
            level = collections.deque() # record from left -> right or right ->left
            for i in range(len(queue)):
                cur_node = queue.popleft()
                # alternate output order
                if zigzag:
                    level.append(cur_node.val)
                else:
                    level.appendleft(cur_node.val)
                # keep bfs traversal order
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(list(level))
            zigzag = not zigzag
        
        return res

# try using traversal approach
