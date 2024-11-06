class Solution(object):
    def kthSmallest(self, matrix,k):
        list=[e for sublist in matrix for e in sublist]
        list.sort()
        return list[k-1]