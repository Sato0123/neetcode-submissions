from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [v for v, f in Counter(nums).most_common(n=k)]
