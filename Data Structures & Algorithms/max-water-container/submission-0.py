from typing import List


class Solution:
    # brute force
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                height = min(heights[i], heights[j])
                width = (j + 1) - (i + 1)
                max_area = max(height * width, max_area)
        return max_area

