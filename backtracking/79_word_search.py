class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # run dfs only at positions that match starting index,
        if not word or not board:
            return False

        row, col = len(board), len(board[0])
        res = [False]
        visited = set()

        def backtrack(r, c, cur_word):
            if r not in range(row) or c not in range(col) or (r,c) in visited:
                return 
            nxt_word = cur_word + board[r][c]
            visited.add((r,c))
            if nxt_word == word:
                res[0] = True
                return 
            backtrack(r+1, c, nxt_word)
            backtrack(r-1, c, nxt_word)
            backtrack(r, c+1, nxt_word)
            backtrack(r, c-1, nxt_word)
            visited.remove((r,c))
    
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    backtrack(r,c,"")
        return res[0]
                        

        
