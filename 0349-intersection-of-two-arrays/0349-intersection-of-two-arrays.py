class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        result = []

        for num in set2:
            if num in set1:
                result.append(num)
                
        return result