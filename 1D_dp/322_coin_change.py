class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start with base case amount = 0, fewest coins needed to reach 0 (0 coins)
        # BFS for finding shortest path, need visited?
        # prioritize minimum difference between current amount and target amount 
        import heapq
        visited = dict()
        queue = []
        heapq.heappush(queue, (amount,0))

        while queue:
            diff_num, num_coins = heapq.heappop(queue)
            #print(num_coins, diff_num)
            
            if diff_num == 0:
                return num_coins
            
            for coin in coins:
                nxt_diff = diff_num - coin
                nxt_coins = num_coins + 1
                if diff_num >= 0:
                    heapq.heappush(queue, (nxt_diff, nxt_coins))
        
        return -1
