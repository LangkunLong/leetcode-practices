class TrieNode:
    def __init__(self):
        self.children = dict()
        self.eow = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # step 1, reorganize words into a prefix trie
        # step 2, at each position on the grid, run recursive dfs to see how many words we can recreate
        # HAVE TO PRUNE THE PREFIX TREE TO SOLVE OPTIMALLY
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
                    child = node.children[ch]
                    board[r][c] = '#' # mark as visited

                    if child.eow:
                        res.add(cur_word)
                        # if marking the end of a trie branch, prune it so we don't need to traverse again
                    for dx, dy in neigh_dir:
                        nx, ny = r + dx, c + dy
                        if nx in range(len(board)) and ny in range(len(board[0])) and board[nx][ny] != '#':          
                            dfs(r+dx, c+dy, child, cur_word)
                    board[r][c] = ch
                    if not child.children:
                        del node.children[ch]
                
                dfs(i, j, root, "")
        
        return list(res)




