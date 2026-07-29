from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n):
            if (
                i > 0 and nums[i - 1] == nums[i]
            ):  # 重複削除 固定値iのペアはすでに見つけている
                continue

            left = i + 1
            right = n - 1
            target = -(nums[i])
            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum > target:
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif twoSum < target:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                else:
                    result.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

        return result
