# min number of coins, shortest path problem, trying BFS solution:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start with base case amount = 0, fewest coins needed to reach 0 (0 coins)
        # BFS for finding shortest path, use dictionary to keep track of fewest coins found for that amount
        import heapq
        visited = dict()
        queue = []
        visited[0] = 0
        heapq.heappush(queue, (0,0))

        while queue:
            num_coins, cur_sum = heapq.heappop(queue)
            if cur_sum not in visited:
                visited[cur_sum] = num_coins
            else:
                visited[cur_sum] = min(visited[cur_sum], num_coins)
            if cur_sum == amount:
                return num_coins
            
            for coin in coins:
                nxt_sum = cur_sum + coin
                nxt_coins = num_coins + 1
                heapq.heappush(queue, (nxt_coins, nxt_sum))
        
        return -1


         
