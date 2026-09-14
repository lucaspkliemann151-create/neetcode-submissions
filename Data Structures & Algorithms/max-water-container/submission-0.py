class Solution:
    def maxArea(self, heights: List[int]) -> int:
        esq = 0
        dir = len(heights)-1
        largest = 0
        while esq < dir:
            area = (dir - esq) * min(heights[esq], heights[dir])
            if area > largest:
                largest = area
            if heights[esq] < heights[dir]:
                esq +=1
            else:
                dir -=1
        return largest