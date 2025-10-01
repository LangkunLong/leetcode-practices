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
            print("form_quad called with", l, w, n)
            # if n < 1:
            #     return None
            # if n == 1:
            #     return Node(grid[l][w], True, None, None, None, None)
            # don't need the above because leaf node definition does not depend on dimension, we only have lead if in 
            # an nxn subgrid we don't have unform values

            # if n == 1, check squad will return true and we will return, as longas n is nonzero it is valid
            if check_quad(l, w, n):
                return Node(grid[l][w], True, None, None, None, None)
            else:

                # Double check indexes, make sure to print them 
                topLeft = form_quad(l, w, n//2)
                topRight = form_quad(l, w + n//2, n//2)
                bottomLeft = form_quad(l + n//2, w, n//2)
                bottomRight = form_quad(l + n//2, w + n//2, n//2)
                return Node(grid[l][w], False, topLeft, topRight, bottomLeft, bottomRight)
        
        def check_quad(l, w, n):
            #print("check_quad called with", l, w, n)
            start = grid[l][w]
            check = True
            for r in range(n):
                for c in range(n):
                    if grid[l + r][w + c] != start:
                        check = False
            #print("check_quad:", check)
            return check
        
        return form_quad(0, 0, len(grid))
