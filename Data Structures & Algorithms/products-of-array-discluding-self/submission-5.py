class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] *= nums[i - 1] * output[i - 1]
        
        toMultiply = 1
        for j in range(len(nums) - 2, -1, -1):
            toMultiply *= nums[j+1]
            output[j] *= toMultiply
        
        return output
            
            