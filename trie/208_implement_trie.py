class Trie:
    from collections import defaultdict

    def __init__(self):
        self.prefix_list = defaultdict(list)
        self.word_list = defaultdict(bool)

    def insert(self, word: str) -> None:
        if word not in self.word_list:
            for i in range(len(word) - 1):
                self.prefix_list[word[:i+1]].append(word[:i+2])
                #print(self.prefix_list)
            self.prefix_list[word].append(None)
            self.word_list[word] = True

    def search(self, word: str) -> bool:
        if word in self.word_list:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefix_list:
            return True
        else:
            return False

# using a linked-list / tree-like approach:
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char] # update trie
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.eow == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
