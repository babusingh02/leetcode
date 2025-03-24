class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        dp=[0]*(len(prizePositions)+1)
        res=0
        j=0
        for i,a in enumerate(prizePositions):
            while prizePositions[j]<prizePositions[i]-k:
                j+=1
            dp[i+1]=max(dp[i],i-j+1)
            res=max(res,i-j+1+dp[j])
            
        return res     
                
                
        