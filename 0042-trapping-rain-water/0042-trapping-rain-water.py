class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft, maxRight=[0], [0]*len(height)
        minLeftAndRight= []
        maxL, maxR= 0, 0
    
        for i in  range(len(height)):
            if i >0:
                if height[i-1] > maxL:
                    maxL=height[i-1]
                    maxLeft.append(maxL)
                else:
                    maxLeft.append(maxL)
        for i in range(len(height) -1, -1,-1):

            if i < len(height)-1:
                if height[i+1] > maxR:
                    maxR=height[i+1]
                    maxRight[i] = maxR
                else:
                    maxRight[i] = maxR
        
        for i in range(len(maxLeft)):
            minNum= min(maxLeft[i], maxRight[i])
            minLeftAndRight.append(minNum)
        ans= 0
        for i in range(len(height)):
            if minLeftAndRight[i] - height[i] <=0:
                continue
            else:
                ans+= minLeftAndRight[i] - height[i] 
        return ans


    



        
        