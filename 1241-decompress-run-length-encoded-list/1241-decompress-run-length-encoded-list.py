class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(nums),2):
            f=nums[i]
            v=nums[i+1]
            res.extend(f*[v])
        return res