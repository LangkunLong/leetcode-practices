# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # by default root is the largest common ancestor
        # can we find any node that is a parent of p and q, including itself
        # what type traversal bfs or dfs? since we need the lowest level, dfs
        # ex: [3,5], [3,1], lca = 3

        # brute force solution: find all path from root to p and q and find LCA
        if not root:
            return None

        lca_node = root
        p_nodes = self.helper(root, p)
        q_nodes = self.helper(root, q)
        p_ptr, q_ptr = 0,0
        while p_ptr in range(len(p_nodes)) and q_ptr in range(len(q_nodes)):
            if p_nodes[p_ptr].val != q_nodes[q_ptr].val:
                break
            lca_node = p_nodes[p_ptr]
            p_ptr += 1
            q_ptr += 1
        
        return lca_node

    def helper(self, head, target):
        path_nodes = []
        found = [False]  # Use mutable to track if target is found

        def recursion(cur):
            if not cur or found[0]:
                return
            path_nodes.append(cur)
            print(cur.val)
            if cur.val == target.val:
                found[0] = True
                return
            recursion(cur.left)
            recursion(cur.right)
            if not found[0]:
                path_nodes.pop()  # if this path doesn't lead to target

        recursion(head)
        return path_nodes

    # optimized approach, we know that if a root is an LCA of p and q, both p and q must be included in subpaths
        # going from root to the leaf nodes either in left or right child or both, when a root returns non-null, 
        # we know it either contains both p and q or 1 of them, so can then search the other child 
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_tree = self.lowestCommonAncestor(root.left, p, q)
        right_tree = self.lowestCommonAncestor(root.right, p, q)
        if left_tree and right_tree:
            return root
        elif left_tree:
            return left_tree
        else:
            return right_tree
        
        if left_tree and right_tree:
            return root
