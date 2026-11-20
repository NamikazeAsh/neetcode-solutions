class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        sol=0

        while i<j:
            l=j-i
            h=min(heights[i],heights[j])
            a=l*h

            if a>sol: sol=a

            if heights[i]>heights[j]: j-=1

            elif heights[j]>heights[i]: i+=1

            elif heights[i]==heights[j]: j-=1

        return sol