# Max heap for smaller numbers
# Min heap for bigger numbers 
# Find Median
import heapq, small, large
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here"""
        self.small, self.large = [], []

    def addNum(self, num:int) -> None:
        heapq.heappush(small, -1 * num)
        if (small and large and 
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(small) >len(large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(large) > len(small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(small) > len(large):
            return self.small[0]
        if len(large) > len(small):
            return self.large[0]
        return (self.small[0] + self.large[0]) / 2