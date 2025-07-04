def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # by default root is the largest common ancestor
        # can we find any node that is a parent of p and q, including itself
        # what type traversal bfs or dfs? since we need the lowest level, dfs
        # ex: [3,5], [3,1], lca = 3
        if not root:
            return None

        lca_node = root
        p_nodes = self.helper(root, p)
        q_nodes = self.helper(root, q)
        p_ptr, q_ptr = 0
        while p_ptr in range(len(p_nodes)) and q_ptr in range(len(q_nodes)):
            if p_nodes[p_ptr].val != q_nodes[q_ptr].val:
                break
            lca_node = p_nodes[p_ptr]
            p_nodes += 1
            q_ndoes += 1
        
        return lca_node

    def helper(self, head, target, path_nodes):
        path_nodes = []
        while head:
            if not head:
                return 
            path_nodes.append(head)
            if head.val == target.val:
                return 
            self.helper(head.left, target)
            self.helper(head.right, target)
        return path_nodes
