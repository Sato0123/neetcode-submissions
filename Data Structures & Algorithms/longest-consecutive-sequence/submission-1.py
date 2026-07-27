from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_set_sorted = sorted(nums_set)

        longest = 0
        current_chain = 0
        prev = None
        for v in nums_set_sorted:
            if prev is None:
                current_chain += 1
                prev = v
                longest = max(longest, current_chain)
                continue

            if v - 1 == prev:
                current_chain += 1
                prev = v
                longest = max(longest, current_chain)
                continue
            else:
                current_chain = 1
                prev = v
        return longest

