from collections import defaultdict
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if (1 not in arr) and (0 not in arr) and (2 not in arr):
            return ""
        dictionary = defaultdict(list)
        ans = ""
        if 2 in arr:
            dictionary[2] = []
            x = arr.index(2)
            if x != 0:
                dictionary[2].append(arr[0])
            if x != 1:
                dictionary.add(2,arr[1])
            if x != 2:
                dictionary[2].append(arr[2])
            if x != 3:
                dictionary[2].append(arr[3])
            d = dictionary[2]
            if 3 in d:
                dictionary[2].remove(3)
                x,y = dictionary[2]
                if x > y and x <= 5:
                    ans = ans + "2" + "3" + ":" + str(x) + str(y)
                else:
                    ans = ans + "2" + "3" + ":" + str(y) + str(x)
                return ans
            #2,1,0
                
        elif 1 in arr:
            arr.index(1)
        elif 0 in arr:
            arr.index(0)
        
        
        