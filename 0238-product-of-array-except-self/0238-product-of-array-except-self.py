class Solution(object):
    def productExceptSelf(self, nums):
        LS=[1]*len(nums)
        RS=[1]*len(nums)
        arr=[0]*len(nums)

        for i in range(1,len(nums)):
            LS[i]=LS[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            RS[i]=RS[i+1]*nums[i+1]

        for i in range(len(nums)):
            arr[i]=LS[i]*RS[i]

        return arr
        