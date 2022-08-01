class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        difference = 0
        sqdifff = 0
        thesum = 0
        for i in range(len(nums)):
            diff = (i+1) - nums[i]
            sqdiff = ((i+1)*(i+1))- (nums[i]*nums[i])
            difference += diff
            sqdifff += sqdiff
        thesum = sqdifff/difference
        return (int(thesum-difference)//2,int(thesum+difference)//2)
        