class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh = 0

        def get_neighbours(node):
            r, c = node
            d_row = [0, 1, 0, -1]
            d_col = [1, 0, -1, 0]
            ans = []
            for i in range(len(d_row)):
                if (0 <= r + d_row[i] < ROWS) and (0 <= c + d_col[i] < COLS):
                    ans.append((r + d_row[i], c + d_col[i]))
            return ans

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 1
        while queue:
            n = len(queue)
            pre_fresh = fresh
            print(pre_fresh)
            for _ in range(n):
                fruit = queue.popleft()

                for neighbour in get_neighbours(fruit):
                    if neighbour in visited:
                        continue
                    
                    nr, nc = neighbour
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        fresh -= 1
            
            print(pre_fresh, fresh)
            if fresh == pre_fresh and fresh != 0:
                return -1
            
            if fresh == 0:
                return minutes

            minutes += 1
        
        return minutes if fresh == 0 else -1


            
        