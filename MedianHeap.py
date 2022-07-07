# Max heap for smaller numbers
# Min heap for bigger numbers 
# Find Median

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here"""
        self.small, self.large = [], []

    def addNum(self, num:int) -> None:
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and self.small[0])

    def findMedian(self) -> float:
