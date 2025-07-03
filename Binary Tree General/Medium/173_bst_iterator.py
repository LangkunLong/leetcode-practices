# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    from collections import deque

    # brute force
    # assume we are given a BST, store everything inorder with a queue; O(1) removal; O(N) space, stores everynode
    # def __init__(self, root: Optional[TreeNode]):
    #     self.queue = deque()
    #     def helper(node):
    #         if not node:
    #             return
    #         helper(node.left)
    #         self.queue.append(node.val)
    #         helper(node.right)
    #     helper(root)
        
    # # returns current smallest element
    # def next(self) -> int:
    #     return self.queue.popleft()
        
    # # is there 
    # def hasNext(self) -> bool:
    #     return len(self.queue) != 0

    # optimized: all tree problems are either DFS or BFS, to have O(h) space, don't have to store all the nodes, 
    # only need to store the nodes needed when we call next(): store just the left subtree first since that is 
    # where the smaller nodes live, then after we pop, traverse the right subtree (since now bigger then root), and
    # it is where the next biggest nodes live, we then put it in the stack (or queue? cannot use a queue because we
    # are inserting the root first (to access right child), so if we popleft it is not the smallest node)
    # dfs uses iterative stack or recursion 
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left
        
    # returns current smallest element
    def next(self) -> int:
        smallest = self.stack.pop()
        # check if node has any right sub-child
        cur = smallest.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return smallest.val
        
    # is there 
    def hasNext(self) -> bool:
        return len(self.stack) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()