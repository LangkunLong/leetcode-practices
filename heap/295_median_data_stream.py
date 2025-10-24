class MedianFinder:
    # can find median by organizing 'sorted' array into 2 heaps, a maxheap of small elements and a minheap or large elements
    # where all elements in small heap is <= all elements of large heap 
    # median: if both heaps are same size, get biggest element from small heap + smallest element from large heap
    # if 1 is bigger, return either the biggest / smallest element of that heap 
    import heapq

    def __init__(self):
        self.max_heap = [] # small array
        self.min_heap = [] # large array 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num) # push to small heap by default
        
        # need to check if heaps are balanced, if not, need to move elements across heaps
        if len(self.max_heap) - len(self.min_heap) > 1:
            biggest_small_num = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, biggest_small_num)
        
        # if biggest elements in small heap bigger than big heap, then need to move that element into the big heap
        if self.max_heap and self.min_heap and (-1 * self.max_heap[0]) > self.min_heap[0]:
            biggest_small_num = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, biggest_small_num)
        
        if len(self.min_heap) - len(self.max_heap) > 1:
            smallest_big_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * smallest_big_num)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return ( (-1 * self.max_heap[0]) + self.min_heap[0]) / 2

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()