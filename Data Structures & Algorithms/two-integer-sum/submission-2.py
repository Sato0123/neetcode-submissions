class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for i2, v2 in enumerate(nums[i + 1:]):
                if v + v2 == target:
                    return [i, i + i2 + 1]
