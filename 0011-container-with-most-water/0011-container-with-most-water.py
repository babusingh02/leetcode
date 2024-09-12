class Solution(object):
    def maxArea(self, height):
        max_area=0
        L=0
        R=len(height)-1
        while L<R:
            area=min(height[L],height[R])*(R-L)
            max_area=max(area,max_area)
            if height[L]<height[R]:
                L+=1
            else:
                R-=1

        return max_area        

        """
        :type height: List[int]
        :rtype: int
        """
        