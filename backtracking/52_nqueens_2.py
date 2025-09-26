class Solution:
    def totalNQueens(self, n: int) -> int:

        res = [0]
        row_set, diag_set, diag2_set = set(), set(), set()
        h_dict = dict()

        def backtrack(c, board, board_hash):
            if c == n:
                h_key = "".join(str(board_hash))
                if h_key not in h_dict:
                    h_dict[h_key] = True
                    res[0] += 1
                return 
            for r in range(n):
                if board_safe(r, c):
                    # mark current elements
                    board_hash.append((r+c))
                    row_set.add(r)
                    diag_set.add(r-c)
                    diag2_set.add(r+c)
                    board[r][c] = 'Q'
                    backtrack(c + 1, board, board_hash)
                    # return, unmark elements
                    board_hash.pop()
                    row_set.remove(r)
                    diag_set.remove(r-c)
                    diag2_set.remove(r+c)
                    board[r][c] = '.'
            
        def board_safe(r, c):
            if (r+c) in diag2_set or (r-c) in diag_set or r in row_set:
                return False
            return True
        
        start = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, start, [])

        return res[0]

