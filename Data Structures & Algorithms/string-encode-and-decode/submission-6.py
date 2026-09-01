class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s = s + str(len(i)) + '#'+ i
        return s

    def decode(self, s: str) -> List[str]:
        strDecoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            current_str = s[j+1 : j+1+length]
            strDecoded.append(current_str)            
            i = j + 1 + length 
        return strDecoded