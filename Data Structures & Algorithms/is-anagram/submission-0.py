class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {c: 0 for c in s}
        dict_t = {c: 0 for c in t}

        for c in s:
            dict_s[c] += 1
        for c in t:
            dict_t[c] += 1

        return dict_s == dict_t      