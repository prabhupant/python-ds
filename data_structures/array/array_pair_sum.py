def arrayPairSum(self, nums: List[int]) -> int:
       nums.sort()
       x = 0
       i=0
       while(i<len(nums)):
           x+=min(nums[i],nums[i+1])   
           i+=2
       return(x)
