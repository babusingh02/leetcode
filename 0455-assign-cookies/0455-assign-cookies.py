class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        content_children=0
        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                content_children+=1
                i+=1
            j+=1
        return content_children
        
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        