class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_res = {}

        for st in strs:
            sorted_st = ''.join(sorted(st))
            if dict_res.get(sorted_st) is not None:
                dict_res[sorted_st].append(st)
            else:
                dict_res[sorted_st] = [st]

        return list(dict_res.values())