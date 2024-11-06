class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d=dict()
        v=97
        for i in key:
            if i !=' ':
                if i not in d.keys():
                   d[i]=chr(v)
                   v +=1
        d[' ']=' '
        res=''
        for i in message:
            res+=d[i]
        return res

        