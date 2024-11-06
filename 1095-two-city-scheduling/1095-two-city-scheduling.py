class Solution(object):
    def twoCitySchedCost(self, costs):
        cost_sorted=sorted(costs,key=lambda x:x[0]-x[1])
        c1=0
        c2=0
        for i in range(len(cost_sorted)//2):
            c1+=cost_sorted[i][0]
        for i in range(len(cost_sorted)//2,len(cost_sorted)):
            c2+=cost_sorted[i][1]
        return c1+c2
        