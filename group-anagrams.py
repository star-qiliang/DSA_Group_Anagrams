class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for x in strs:
            k = ''.join(sorted(x))
            if k in strs_dict:
                strs_dict[k].append(x)
            else:
                strs_dict[k] = [x,]
        res_list = [v for v in strs_dict.values()]
        return res_list

