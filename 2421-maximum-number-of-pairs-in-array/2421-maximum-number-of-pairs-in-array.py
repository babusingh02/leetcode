from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        a = Counter(nums)
        print(a)
        
        lst1 = []
        lst2 = []

        for i, j in a.items():
            if j % 2 == 0:
                lst1.extend([i] * (j//2))
            else:
                if j // 2 != 0:
                    lst1.extend([i] * (j//2))
                if j % 2 == 1:
                    lst2.append(i)
        return [len(lst1), len(lst2)]