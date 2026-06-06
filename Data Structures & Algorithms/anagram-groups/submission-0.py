class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        final_lst = list()
        for i, n in enumerate(strs):
            sorted_string = sorted(n)
            final_string = "".join(sorted_string)
            if dct.get(final_string) == None:
                dct[final_string] = [n]
            else:
                dct.get(final_string).append(n)
        for items in dct.values():
            final_lst.append(items)

        return final_lst
