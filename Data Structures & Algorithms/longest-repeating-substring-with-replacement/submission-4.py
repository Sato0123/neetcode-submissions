from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        chars = defaultdict(int)
        longest = 0
        n = len(s)

        while right < n:
            chars[s[right]] += 1
            mode = max(chars.values())
            K = (right - left + 1) - mode
            if K <= k:
                right += 1
            else:
                chars[s[left]] -= 1
                right += 1
                left += 1
            longest = max(longest, right - left)

        return longest
