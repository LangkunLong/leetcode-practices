# still failing tle after changing to in-grid marking

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # step 1, reorganize words into a prefix trie
        # step 2, at each position on the grid, run recursive dfs to see how many words we can recreate
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.eow = True
        
        # recursive dfs
        # need to traverse both the trie and the grid, at each position, run dfs
        neigh_dir = [(0, 1), (0,-1), (1, 0), (-1, 0)]
        res = set() # can have different paths forming the same word
        for i in range(len(board)):
            for j in range(len(board[i])):
                def dfs(r, c, node, cur_word):
                    # base case: out of bounds or starting prefix doesn't exist
                    ch = board[r][c]
                    if ch not in node.children:
                        return 
                    # backtracking: mark as visited in current path, then un-mark it when we return
                    cur_word += board[r][c]
                    node = node.children[board[r][c]]
                    board[r][c] = '#' # mark as visited

                    if node.eow:
                        res.add(cur_word)
                    for dx, dy in neigh_dir:
                        nx, ny = r + dx, c + dy
                        if nx in range(len(board)) and ny in range(len(board[0])) and board[nx][ny] != '#':          
                            dfs(r+dx, c+dy, node, cur_word)
                    board[r][c] = ch
                
                dfs(i, j, root, "")
        
        return list(res)




