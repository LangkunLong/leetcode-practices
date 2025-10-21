class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        # python default min_heap
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        max_heap = []
        heapq.heapify(min_heap)

        for i in range(k):
            while min_heap and min_heap[0][0] <= w:
                do_venture = heapq.heappop(min_heap)[1]
                heapq.heappush(max_heap, -1 * do_venture)
            
            if max_heap:
                w += -1 * heapq.heappop(max_heap)
        
        return w
