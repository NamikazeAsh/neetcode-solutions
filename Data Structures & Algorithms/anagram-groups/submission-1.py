class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key-dict, val-list of words 
        d={}
        for s in strs:
            d.setdefault(str(sorted(s)),[]).append(s)
        return (list(d.values()))
        