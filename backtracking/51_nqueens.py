class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # recursively try out all board combinations by placing 1 queen at a time

        # recursing over columns: 
        # for every column, try place a queen at every row, 
        # if valid, we recurse and try to place the next queen at the next colum
        res = []
        def backtrack(col, board):
            # base case: if we reach index n, we filled column (n-1) so we filled all queens
            if col == n:
                res.append(board)
                return 
            for row in range(n):
                if queen_safe(row, col, board):
                    board[row][col] = 'Q'
                    backtrack(col + 1, board)
                    board[row][col] = '' # BACKTRACK, have to remove the placed Queen
        
        # since we are placing column by column, only need to check the columns towards the left
        def queen_safe(row, col, board):
            # diagonal
            cur_row, cur_col = row, col
            while cur_row in range(n) and cur_col in range(n):
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
                cur_col -= 1
            
            cur_row = row
            while cur_row in range(n):
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_row -= 1
            
            cur_col = col
            while cur_col in range(n):
                if board[cur_row][cur_col] == 'Q':
                    return False
                cur_col -= 1
            return True
        
        board = [['' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)

        return res


# incorrect output:
"""
[[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]],[["","","",""],["","","",""],["","","",""],["","","",""]]]
"""
