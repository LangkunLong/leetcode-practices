class TrieNode:
    def __init__(self):
        self.children = dict()
        self.eow = False

class WordDictionary:
    from collections import deque

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        # same approach as previous question
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.eow = True

    def search(self, word: str) -> bool:
        # need to use dfs recursive backtracking because might go down all 
        # possible prefixes 

        def dfs(j, node):
            cur = node
            # go through all remaining letters
            for i in range(j, len(word)):
                char = word[i]
                if char == '.':
                    # need to traverse all the children prefixes
                    for prefix in cur.children.values():
                        if dfs(i + 1, prefix):
                            return True
                    return False
                else:
                    # base case, just regular update node
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            # traversed all letters, check if eow
            return cur.eow

        return dfs(0, self.root)
            
        

            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
