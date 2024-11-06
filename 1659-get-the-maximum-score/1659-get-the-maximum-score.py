class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        while nums1 and nums2:
            if nums1[-1] == nums2[-1]:
                sum1 = sum2 = max(sum1, sum2) + (nums1.pop()+nums2.pop())//2
            else:
                sum1, sum2 = (sum1 + nums1.pop(), sum2) if nums1[-1] > nums2[-1] else (sum1, sum2 + nums2.pop())

        return max(sum1 + sum(nums1), sum2 + sum(nums2)) % (10**9+7)