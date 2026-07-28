from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)

        longest = 1

        for n in nums_set:
            if n - 1 in nums_set:
                continue

            current = n
            chain = 1

            while current + 1 in nums_set:
                chain += 1
                current += 1
                n += 1

                longest = max(chain, longest)

        return longest
