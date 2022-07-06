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
            #end current iteration of loop and continues to next
            if nums[i] <= nums[i+1]:
                continue
            #checks if the one number edit works for the other numbers
            if changed:
                return False
            # [ 3 , 4 , 2 ]
            # [i-1, i ,i+1]
            # [ 3 , 3 , 2 , 4 ]
            if i==0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True
        return True
