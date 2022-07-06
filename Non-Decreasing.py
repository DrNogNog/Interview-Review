#  4 3 3 4 
# When decreasing numbers, always decrease it from the left to right, because
# of the english words "non-decreasing"

class Solution:
    #check_Possibility is snake case
    #this is camel case
    def checkPossibility(self,nums: List[int]) -> bool:
        #checks if the one number edit has been edited
        changed = False
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False
