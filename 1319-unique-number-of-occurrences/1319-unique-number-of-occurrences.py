"""
Observations:
1) Non empty arr

Thoughts:
1) We basically do {elem: count} then iterate and populate a set with counts
and if we find a count already in there that means a non-unique count has been found,
return False. Otherwise all unique so return True

Time: O(2n) = O(n)
Space: O(2n) = O(n)
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = {}

        for num in arr:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1

        return len(set(num_count.values())) == len(num_count.values())
        