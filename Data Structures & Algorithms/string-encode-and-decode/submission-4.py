from typing import List

SEP = "/"
END = "#"


class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(([str(len(s)) + SEP for s in strs] + [END] + [s for s in strs]))

    def decode(self, s: str) -> List[str]:
        header = s[: s.find(END) + 1].split(f"{SEP}")
        body = s[s.find(END) + 1 :]
        ret_list = []

        # print(header)
        # print(body)
        #
        left = 0
        right = 0
        for length_str in header:
            if length_str == END:
                return ret_list
            right += int(length_str)
            ret_list.append(body[left:right])
            left = right

        raise ValueError("Invalid format")
