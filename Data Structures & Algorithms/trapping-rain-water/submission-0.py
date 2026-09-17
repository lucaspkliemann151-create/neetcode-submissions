class Solution:
    def trap(self, height: List[int]) -> int:
        esq = 0
        dir = len(height) -1
        count = 0
       
        maxLeft = height[esq]
        maxDir = height[dir]
        while esq != dir:
            if maxLeft < maxDir:
                esq+=1
                if height[esq] > maxLeft:
                    maxLeft = height[esq]
                else:
                    count += (maxLeft - height[esq])
            else:
                dir-=1
                if height[dir] > maxDir:
                    maxDir = height[dir]
                else:
                    count += (maxDir - height[dir])
        return count