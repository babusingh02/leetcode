class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in strs:
            s=list(i)
            s.sort()
            k=''.join(s)
            if k not in d:
                d[k]=[i]
            else:
                d[k]+=[i]
        return list(d.values())
        
        