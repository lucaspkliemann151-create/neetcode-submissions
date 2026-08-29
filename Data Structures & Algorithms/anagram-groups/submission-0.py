class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        norma = {}
        for i in strs:
            normalS = ''.join(sorted(i))
            if (normalS) in norma:
                norma[normalS].append(i)
            else:
                norma[normalS] = [i]
        return list(norma.values())
                