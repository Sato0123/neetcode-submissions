class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 in nums_set:
                continue

            chain = 1

            while n + chain in nums_set:
                chain += 1

            longest = max(chain, longest)

        return longest
