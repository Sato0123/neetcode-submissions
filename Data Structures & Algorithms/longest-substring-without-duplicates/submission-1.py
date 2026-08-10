class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        chars = set()
        left, right = 0, 0
        while right < n:
            if (char := s[right]) not in chars:
                chars.add(char)
                longest = max(longest, len(chars))
            else:
                while s[left] != s[right]:
                    chars.discard(s[left])
                    left += 1
                left += 1
            right += 1
        print(chars)
        return longest
