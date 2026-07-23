from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [v for v, f in Counter(nums).most_common(n=k)]
