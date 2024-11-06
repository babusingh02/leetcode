class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right = sum(nums)
        left = 0
        ans = []
        for num in nums:
            right -= num
            ans.append(abs(left-right))
            left += num
            
        
        return ans