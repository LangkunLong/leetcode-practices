class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # step 1, process board into adj_list, keep track of letter occurrence
        # step 2, recursive backtracking

        # create adj_list based on neighbors
        from collections import defaultdict
        neigh_list = defaultdict(list)
        word_positions = defaultdict(list)
        neigh_dir = [(0, 1), (0,-1), (1, 0), (-1, 0)]
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                for dx, dy in neigh_dir:
                    if i + dx in range(len(board)) and j + dy in range(len(board[i])):
                        key_str = board[i][j] + str(i) + str(j) # can reconstruct this given word_positions  
                        if key_str not in neigh_list:
                            neigh_list[key_str].append(board[i+dx][j+dy])
                            word_positions[board[i][j]].append((i,j))
        #print(neigh_list)
        #print(word_positions)

        # traverse using backtracking
        res = []
        for word in words:
            target = word
                
            def dfs(char, cur_word):
                # base case:
                if cur_word == target:
                    return True
                for start_pos in word_positions[char]:
                    key_str = char + str(start_pos[0]) + str(start_pos[1])
                    for neigh in neigh_list[key_str]:
                        dfs(neigh, char + neigh)
            if dfs():
                res.append(word)





