class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #identify top 3 atheletes
        d={}
        res=[]
        descScore=sorted(score,reverse=True)
        for i in range(len(descScore)):
            if i==0:
                d[descScore[i]]="Gold Medal"
            elif i==1:
                d[descScore[i]]="Silver Medal"
            elif i==2:
                d[descScore[i]]="Bronze Medal"
            else:
                d[descScore[i]]=str(i+1)

        for i in range(len(score)):
            res.append(d[score[i]])
        return res
        