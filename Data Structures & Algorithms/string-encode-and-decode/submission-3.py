from collections import deque
from typing import List

SEP = "/"
MAX_DIGITS = 3


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        最初の一文字を除いて、玉ねぎ型のデータ構造になっている
        f"{len_len_list}{len_list_str}{ret_str}"
            len_len_list: リストの要素数
            len_list_str: 文字列の長さの一覧化した文字列
            ret_list: 文字列 (反転して挿入している)
        """
        len_len_list = 0
        len_list = []
        ret_str = ""

        # strつめ作業
        strs.reverse()
        for string in strs:
            len_list.append(len(string))
            ret_str += string[::-1]

        len_len_list = len(len_list)
        len_list_str = ""

        # intつめ作業
        len_list.reverse()
        for len_num in len_list:
            len_list_str += f"{str(len_num)}{SEP}"

        return f"{len_len_list}{SEP}{len_list_str}{ret_str}"

    def decode(self, s: str) -> List[str]:
        strs = deque(s)
        list_len_str = ""
        for _ in range(MAX_DIGITS + 1):
            # 最高でも MAX_DIGITS までしか回さない
            # 0 <= strs.length < 100
            c = strs.popleft()
            if c == "/":
                break
            list_len_str += c
        else:
            raise ValueError("encoding str is broken!")
        list_len = int(list_len_str)

        ret_list = [[] for _ in range(list_len)]

        for i in range(list_len):
            len_str = ""
            for _ in range(MAX_DIGITS + 1):
                # 最高でも MAX_DIGITS までしか回さない
                # 0 <= strs[i].length < 200
                # なので最高3桁までしか来ない。出る時は必ずbreakするようにする
                # +1はSEP分
                len_str_current = strs.popleft()
                if len_str_current == "/":
                    break
                len_str += len_str_current
            else:
                raise ValueError("encoding str is broken!")

            str_item = "".join(strs.pop() for j in range(int(len_str)))
            ret_list[i] = str_item
        return ret_list
