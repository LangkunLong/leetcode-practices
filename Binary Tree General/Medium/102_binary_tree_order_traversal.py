class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal same as bfs
        if not root:
            return []
        
        res = []
        queue = collections.deque()
        queue.append(root)

        while(queue):
            count = len(queue)
            res_level = []
            for i in range(count):
                cur_node = queue.popleft()
                res_level.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(res_level)
        
        return res
