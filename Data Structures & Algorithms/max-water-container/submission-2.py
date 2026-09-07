class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # solution = 0
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         width = j-i
        #         height = min(heights[i],heights[j])
        #         area = height * width
        #         solutions.append(area)
        # return max(solutions)

        sol = 0
        i=0
        j=len(heights)-1
        while j>i:
            w=j-i
            h=min(heights[i],heights[j])
            a=w*h
            if a>sol:
                sol=a
            if heights[i]>heights[j]:
                j-=1
            elif heights[j]>heights[i]:
                i+=1
            elif heights[i]==heights[j]:
                j-=1
        return sol
            