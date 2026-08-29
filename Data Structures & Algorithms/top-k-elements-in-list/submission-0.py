class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else: 
                counter[i] = 1
        counter = dict(sorted(counter.items(), key = lambda item : item[1], reverse = True))

        return list(counter.keys())[:k]