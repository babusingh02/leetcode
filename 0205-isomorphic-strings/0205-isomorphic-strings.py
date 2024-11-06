class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] !=t[i]:
                    return False
        r=dict()
        for i in range(len(t)):
            if t[i] not in r:
                r[t[i]] = s[i]
            else:
                if r[t[i]] !=s[i]:
                    return False
        return True        