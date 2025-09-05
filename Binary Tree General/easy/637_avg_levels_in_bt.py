class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # use bfs, inserting and popping from the queue
        # popleft all the elements in the current level, and append to the queue
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
            res.append(sum(res_level) / len(res_level))
        
        return res
