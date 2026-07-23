class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ret_list = []
        checked = {}

        for i, string in enumerate(strs):
            k = "".join(sorted(string))
            if k in checked.keys():
                checked[k].append(i)
            else:
                checked[k] = [i]

        for k, v in checked.items():
            group = []
            for i in v:
                group.append(strs[i])
            ret_list.append(group)

        return ret_list

