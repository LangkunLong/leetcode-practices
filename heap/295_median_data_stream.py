# can be directly solved with python sortedList, or maps (trees) in c++
class MedianFinder:
    # using sorted list, o(logn) index, insert, remove
    from sortedcontainers import SortedList

    def __init__(self):
        self.stream = SortedList()

    def addNum(self, num: int) -> None:
        self.stream.add(num)

    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2 - 1] + self.stream[n//2]) / 2
        else:
            return self.stream[n // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
