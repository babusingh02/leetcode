class Solution:
    def stringHash(self, s: str, k: int) -> str:
        arr=[]
        for i in range(0,len(s),k):
            arr.append(s[i:i+k])
        res = ''
        for i in arr:
            c=0
            for j in i:
                c += ord(j) - 97
            c=(c%26)
            res +=chr(c+97)
            
        return res

        