class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        li=[]
        n=max(candies)
        for i in range(len(candies)):
            m=candies[i]+extraCandies
            li.append(func(m,n))
        return li
def func(m,n):
    if m>=n:
        return True
    return False