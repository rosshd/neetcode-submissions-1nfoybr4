class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        numHash = {}

        for i, n in enumerate(nums):
            if target - n in numHash:
                return [numHash[target - n], i]
            numHash[n] = i
        return
