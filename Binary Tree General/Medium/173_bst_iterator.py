class BSTIterator:
    from collections import deque

    # assume we are given a BST, store everything inorder with a queue; O(1) removal
    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.queue.append(node.val)
            helper(node.right)
        helper(root)
        
    # returns current smallest element
    def next(self) -> int:
        return self.queue.popleft()
        
    # is there 
    def hasNext(self) -> bool:
        return len(self.queue) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()