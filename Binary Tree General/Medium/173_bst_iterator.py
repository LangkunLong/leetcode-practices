class BSTIterator:

    # assume we are given a BST
    def __init__(self, root: Optional[TreeNode]):
        self.head = root
        self.smallest = next()
        
    # returns current smallest element
    def next(self) -> int:
        smallest = None
        while(self.head):
            if not self.head:
                return 
            self.head = self.head.left
            smallest = self.head.val
            self.head = self.head.right
        return smallest
        
    # is there 
    def hasNext(self) -> bool: