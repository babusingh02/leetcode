class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        heapq.heapify(nums)
        res=[None for i in range(len(nums))]
        idx=0
        while len(nums)>0:
            cur=heapq.heappop(nums)
            res[idx]=cur*cur
            idx+=1
        return res