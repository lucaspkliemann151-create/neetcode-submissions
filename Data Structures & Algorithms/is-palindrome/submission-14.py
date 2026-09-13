class Solution:
    def isPalindrome(self, s: str) -> bool:
        esq = 0
        right = len(s) - 1 

        while esq < right:
            while esq < right and not s[esq].isalnum():
                esq +=1
            while esq < right and not s[right].isalnum():
                right -=1
            if s[esq].lower() != s[right].lower():
                return False
            esq +=1
            right -=1
        return True