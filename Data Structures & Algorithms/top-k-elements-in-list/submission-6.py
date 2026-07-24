from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            return []

        counter = Counter(nums)

        # len + 1 文のバケットを作成(添字==頻度)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in counter.items():
            buckets[value].append(key)

        # バケットを頻出順に
        buckets.reverse()

        print(buckets)
        ret_list = []
        cnt = 0
        for bucket in buckets:
            if bucket:
                for f_num in bucket:
                    ret_list.append(f_num)
                    cnt = cnt + 1
            if cnt >= k:
                return ret_list

        return ret_list

