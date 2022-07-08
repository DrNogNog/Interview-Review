# 132 pattern in list

def pattern(list):
    for i in range(1,len(list)-1):
        if list[i+1]<list[i] and list[i-1]<list[i+1]:
            return True
    return False
print(pattern([3,4,3]))

# monotonic Stack
# python 3 
def opt_pattern(self, nums: List[int]) -> bool:
    stack = [] #pair (num,minLeft)
    curMin = nums[0]
    for n in nums[1:]:
        while stack and n>=stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True
        stack.append([n, curMin])
        curMin = min(curMin, n)
    return False