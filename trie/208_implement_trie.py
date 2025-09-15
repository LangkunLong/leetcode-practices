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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
