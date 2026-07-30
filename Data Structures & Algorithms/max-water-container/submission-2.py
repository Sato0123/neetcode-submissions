from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        left, right = 0, n - 1

        while left < right:
            width = right - left
            height = heights[left] if heights[left] < heights[right] else heights[right]

            area = height * width
            max_area = max(area, max_area)

            if height == heights[left]:
                left += 1
            if height == heights[right]:
                right -= 1

        return max_area
