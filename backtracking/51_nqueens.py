class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # recursively try out all board combinations by placing 1 queen at a time

        # recursing over columns: 
        # for every column, try place a queen at every row, 
        # if valid, we recurse and try to place the next queen at the next column
        res = []
        row_set, up_diag_set, down_diag_set = set(), set(), set()
        def backtrack(col, board):
            # base case: if we reach index n, we filled column (n-1) so we filled all queens
            
            if col == n:
                res.append(["".join(row) for row in board]) # remember to deep copy
                return 
            for row in range(n):
                if queen_safe(row, col):
                    #print(board)
                    up_diag_set.add(row-col)
                    down_diag_set.add(row+col)
                    row_set.add(row)
                    board[row][col] = 'Q'
                    backtrack(col + 1, board)
                    board[row][col] = '.' # BACKTRACK, have to remove the placed Queen
                    up_diag_set.remove(row-col)
                    down_diag_set.remove(row+col)
                    row_set.remove(row)
        
        # using optimized set tracking approach:
        def queen_safe(row, col):
            if (row - col) in up_diag_set or (row + col) in down_diag_set or row in row_set :
                return False
            return True
            
        start = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0,start)
        return res
