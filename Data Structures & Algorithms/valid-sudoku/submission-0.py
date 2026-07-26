from collections import Counter
from typing import List


class Solution:
    def check(self, cnt: Counter):
        most = cnt.most_common(2)
        for m in most:
            if "." == m[0]:
                continue
            else:
                # 数値の場合
                if m[1] >= 2:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        # check column
        for i in range(9):
            row = Counter(board[i])
            column = Counter([row[i] for row in board])
            if not self.check(row) or not self.check(column):
                return False

        # check 3*3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for k in range(3):
                    box += board[i + k][j : j + 3]
                box_cnt = Counter(box)
                if not self.check(box_cnt):
                    return False
        return True
