from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_list = [1 for _ in range(len(nums))]
        for i, value in enumerate(nums):
            for j, v in enumerate(nums):
                if i == j:
                    continue
                else:
                    ret_list[i] *= v
        return ret_list
