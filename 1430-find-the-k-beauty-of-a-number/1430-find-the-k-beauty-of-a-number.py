class Solution(object):
    def divisorSubstrings(self, num, k):
        count=0
        s=str(num)
        for i in range (k,len(s)+1):
            div=int(s[i-k:i])
            if div!=0 and num%div==0:
                count+=1
        return count
        
        #:type num: int
        #:type k: int
        #:rtype: int
        
        