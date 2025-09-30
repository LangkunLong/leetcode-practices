"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # we know that n is a multiple of 2, we can form a quadrant of 4s by dividing length by 2, width by 2
        # recursively divide the quadrant until n is 1 or n is 2
        # pass starting length, width starting index for each quadrant and subgrid length

        def form_quad(l, w, n):
            # base case, return None if n is 0
            if n < 1:
                return None
            root = Node()
            if check_quad(l, w, n):
                root.val = (grid[l][w] == 1)
                root.isLeaf = (n == 1)
                print(root.val, root.isLeaf)
                return root
            else:
                # need to recurse
                root.topLeft = form_quad(0, 0, n//2)
                root.topRight = form_quad(0, n//2, n//2)
                root.bottomLeft = form_quad(n//2, 0, n//2)
                root.bottomRight = form_quad(n//2, n//2, n//2)
        
        def check_quad(l, w, n):
            sub_grid = 0
            for r in range(l, n):
                for c in range(w, n):
                    sub_grid += grid[r][c]
            
            return (sub_grid == 0 or sub_grid == (n ** 2))
        
        return form_quad(0, 0, len(grid))

