class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # run dfs only at positions that match starting index,
        # don't need to build full string, can pass position to the word, and check if current
        # board word is equal to ith index
        if not word or not board:
            return False

        row, col = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            # means we checked all characters of the word 
            if i == len(word):
                return True
            if r not in range(row) or c not in range(col) or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            found = backtrack(r+1, c, i+1) or backtrack(r-1, c, i+1) or backtrack(r, c+1, i+1) or backtrack(r, c-1, i+1)
            visited.remove((r,c))

            return found 
    
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(r,c, 0):
                        return True
        
        return False
                        

        
