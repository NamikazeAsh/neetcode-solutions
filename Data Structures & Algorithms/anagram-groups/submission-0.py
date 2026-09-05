class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            word2 = "".join(sorted(word))

            if word2 not in d:
                d[word2] = []
            d[word2].append(word)
        return list(d.values())
