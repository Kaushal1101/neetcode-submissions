class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            freq = math.pow(p[0], 2) + math.pow(p[1], 2)
            # Max heap
            heapq.heappush(heap, (-freq, p))

            if len(heap) > k:
                # Pops largest distance point
                heapq.heappop(heap)
        
        return [p for _, p in heap]
            
