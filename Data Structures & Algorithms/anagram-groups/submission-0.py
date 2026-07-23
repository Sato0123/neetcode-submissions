class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret_list = []
        checked = {}

        for i, string in enumerate(strs):
            k = Counter(sorted(string)).__str__()
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
