from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for string in strs:
            groups["".join(sorted(string))].append(string)
        return list(groups.values())
