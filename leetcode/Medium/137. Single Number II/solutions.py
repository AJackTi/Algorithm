class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictRepeatedly = dict()
        for i in nums:
            if i not in dictRepeatedly:
                dictRepeatedly[i] = 0
            dictRepeatedly[i] += 1
        
        for k, v in dictRepeatedly.items():
            if v == 1:
                return k
        
        return -1
