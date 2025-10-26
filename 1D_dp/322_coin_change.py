class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start with base case amount = 0, fewest coins needed to reach 0 (0 coins)
        # BFS for finding shortest path, need queue and visited set
        # don't need priority queue because each layer of bfs is using 1 coin, bfs explores by number of coin used
        # The first time we encounter remaining amount x, we are using the fewest coins possible to reach it.
        # Any future path that reaches x later must use more coins, so it can never lead to a better solution.

        from collections import deque
        visited = set()
        queue = deque()
        queue.append((amount, 0))

        while queue:
            diff_num, num_coins = queue.popleft()
            visited.add(diff_num)
            
            if diff_num == 0:
                return num_coins
            
            for coin in coins:
                nxt_diff = diff_num - coin
                nxt_coins = num_coins + 1
                if nxt_diff >= 0 and nxt_diff not in visited:
                    queue.append((nxt_diff, nxt_coins))
        
        return -1



         
