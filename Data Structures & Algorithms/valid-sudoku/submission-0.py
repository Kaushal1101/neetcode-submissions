class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        def seen_before(r, c):
            val = board[r][c]
            box = 3 * (r // 3) + (c // 3)
            return val in row_sets[r] or val in col_sets[c] or val in box_sets[box]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif seen_before(r, c):
                    return False
                else:
                    box = 3 * (r // 3) + (c // 3)
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])
                    box_sets[box].add(board[r][c])
        
        return True