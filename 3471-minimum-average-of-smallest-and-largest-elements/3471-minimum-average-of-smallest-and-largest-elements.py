class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n=len(nums)
        r=float('inf')
        nums.sort()
        for i in range(n//2):
            res=(nums[i]+nums[n-i-1])/2
            r=min(r,res)
        return r


        