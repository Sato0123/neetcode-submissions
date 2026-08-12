class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        a = ord('a')
        need = [0] * 26
        win = [0] * 26
        for i in range(n):
            need[ord(s1[i]) - a] += 1
            win[ord(s2[i]) - a] += 1
        if need == win:
            return True

        for i in range(n, m):
            win[ord(s2[i]) - a] += 1        # 右端を追加
            win[ord(s2[i - n]) - a] -= 1    # 左端を削除
            if need == win:
                return True
        return False