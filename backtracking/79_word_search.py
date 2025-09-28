class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # run dfs only at positions that match starting index,
        # or can i run a bfs?
        if not word or not board:
            return False
        
        from collections import deque
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        row, col = len(board), len(board[0])
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    # bfs
                    queue = deque()
                    visited = set()
                    queue.append(((r,c), board[r][c]))
                    while queue:
                        cur_node = queue.popleft()
                        cur_r, cur_c = cur_node[0]
                        cur_word = cur_node[1]
                        
                        if cur_word == word:
                            return True
                        
                        for dx, dy in dirs:
                            nr, nc = cur_r + dx, cur_c + dy
                            if nr in range(row) and nc in range(col) and (nr, nc) not in visited:
                                queue.append(((nr,nc), cur_word + board[nr][nc]))
                                visited.add((nr, nc))
        return False
                        

        
