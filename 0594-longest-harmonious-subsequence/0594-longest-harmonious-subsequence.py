class Solution(object):
    def findLHS(self, nums):
        my_dict=defaultdict(int)
        for num in nums:
            my_dict[num]+=1
            max_=0
        for num in my_dict.keys():
            if my_dict.get(num+1):
                max_=max(max_,my_dict[num]+my_dict.get(num+1))
        return max_