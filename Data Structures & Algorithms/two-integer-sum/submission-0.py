class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        numHash = {}

        for i in range(len(nums)):
            if numHash.get(target - nums[i], -1) != -1:
                result.append(numHash[target - nums[i]])
                result.append(i)
                return result
            numHash[nums[i]] = i
        return []
