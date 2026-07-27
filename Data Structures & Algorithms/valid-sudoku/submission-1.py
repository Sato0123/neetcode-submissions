from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                b = (r // 3) * 3 + c // 3
                if v in row[r] or v in column[c] or v in box[b]:
                    return False

                row[r].add(v)
                column[c].add(v)
                box[b].add(v)
        return True
