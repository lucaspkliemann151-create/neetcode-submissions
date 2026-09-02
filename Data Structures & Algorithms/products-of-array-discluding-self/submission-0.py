class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []
        pre = 1
        for i in reversed(nums):
            postfix.append(i * pre)
            pre = i * pre
        postfix = postfix[::-1]
        pre = 1
        for i in nums:
            prefix.append(i * pre)
            pre = i * pre
        
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output
        
                    
        