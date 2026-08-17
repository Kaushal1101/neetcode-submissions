"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return 0

        interval_heap = [intervals[0].end]
        rooms = 1

        for interval in intervals[1:]:
            if interval.start < interval_heap[0]:
                rooms += 1
            else:
                heapq.heappop(interval_heap)

            heapq.heappush(interval_heap, interval.end)
        
        return rooms