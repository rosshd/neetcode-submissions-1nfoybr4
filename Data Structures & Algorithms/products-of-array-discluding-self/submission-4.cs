public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var totalProduct =0;
        bool isZero = false;
        var output = new int[nums.Length];
        foreach(int num in nums)
        {
            if(num == 0)
            {
                if(isZero)
                {
                    totalProduct = 0;
                }
                else
                {
                    isZero = true;
                }
            }
            else
            {
                if(totalProduct == 0 && !isZero)
                {
                    totalProduct++;
                }
                totalProduct *= num;
            }
        }
        for(int i = 0; i < nums.Length; i++)
        {
            if(isZero && nums[i] != 0)
            {
                output[i] = 0;
            }
            else if(nums[i] == 0)
            {
                output[i] = totalProduct;
            }
            else
            {
                output[i] = totalProduct / nums[i];
            }
        }
        return output;
    }
}
