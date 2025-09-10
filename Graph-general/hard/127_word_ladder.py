class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict, deque

        if endWord not in wordList:
            return 0
        
        # construct adj_list using patterns, key is the pattern, value is the words that match with the pattern
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)
        
        # bfs traversal
        queue = deque()
        visited = set()
        queue.append((beginWord, 1))
        min_path = float('inf')
        found = False
        while queue:
            word, path = queue.popleft()
            visited.add(word)
            if word == endWord:
                return path
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                for seq_word in adj_list[pattern]:
                    if seq_word not in visited:
                        queue.append((seq_word, path + 1))
        
        return 0
        

            

    
        
            
