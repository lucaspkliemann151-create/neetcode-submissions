class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w = sorted(s)
        y = sorted(t)
        return w == y