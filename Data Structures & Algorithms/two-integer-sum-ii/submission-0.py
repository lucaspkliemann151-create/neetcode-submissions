class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     esq = 0
     dir = len(numbers)-1  
     found = False 
     while not found:
        if numbers[esq] + numbers[dir] == target:
            return [esq+1, dir+1]
        elif numbers[esq] + numbers[dir] > target:
            dir-=1
        else:
            esq+=1 