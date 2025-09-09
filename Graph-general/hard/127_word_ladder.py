class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict, deque, Counter

        if endWord not in wordList:
            return 0
        
        # construct graph using wordlist
        adj_list = defaultdict(list)
        queue = deque()
        visited = set()
        queue.append(beginWord)
        while queue:
            cur = queue.popleft()
            visited.add(cur)
            for word in wordList:
                if self.validSeq(cur, word) and word not in visited:
                    adj_list[cur].append(word)
                    queue.append(word)
        #print(adj_list)
        
        # bfs with priority queue, need to evaluate the 'fastest' transformation
        queue.clear()
        visited.clear()
        queue.append((beginWord, 1))
        min_path = float('inf')
        found = False
        while queue:
            n, w = queue.popleft()
            visited.add(n)
            if n == endWord:
                min_path = min(min_path, w)
                found = True
            for seq in adj_list[n]:
                if seq not in visited:
                    queue.append((seq, w + 1))
        
        if found:
            return min_path
        else:
            return 0
        
    
    # determine if 2 words differ by 1 letter, use frequency counter
    def validSeq(self, src, dst):
        diff = 0
        if src != dst: # prevent repeat cycles in case beginword is in wordlist
            for x, y in zip(src, dst):
                if x != y:
                    diff += 1
        return diff == 1
            

    
        
            
