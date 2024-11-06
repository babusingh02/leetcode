class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        row,count_one=0,0
        for i in range(n):
            one=0
            for j in range(m):
                if mat[i][j]==1:
                    one+=1

            if one>count_one:
                count_one=one

                row=i

        return [row,count_one]                