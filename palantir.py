from sqlite3 import Row


table = [
[0,0,0,0,0],
[0,0,-1,0,0],
[-1,0,-1,0,0],
[0,0,0,0,0],
[0,0,-1,-1,0],
[0,-1,0,0,-1]
]

tuple = (2,3)

def solution(table, x):
    range_row = len(table)-1
    col_row = len(table[0])-1
    ans = []
    if not (x[0]+1 > range_row and x[1] > col_row):
        if table[x[0]+1][x[1]] != -1:
            ans.append((x[0]+1,x[1],"1"))
    if not (x[0]-1 > range_row and x[1] > col_row):
        if table[x[0]-1][x[1]] != -1:
            ans.append((x[0]-1,x[1],"2"))
    if not (x[0] > range_row and x[1]+1 > col_row):
        if table[x[0]][x[1]+1] != -1:
            ans.append((x[0],x[1]+1,"3"))
    if not (x[0] > range_row and x[1]-1 > col_row):
        if table[x[0]][x[1]-1] != -1:
            ans.append((x[0],x[1]-1,"4"))
    print(ans)
    return ans

solution(table,tuple)


def code(x):
    count = 0
    while x > 0:
        x = x // 10
        result = x % 7
        if (result % 7 )== 0:
            count += 1
    return count

def partition(arr, low, high):
    # Choose the right most element as pivot
    pivot = arr[high]
    #Pointer for greater element
    i = low-1
    #Traverse thru all elem compare each with pivot
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j],arr[i])
    (arr[i+1],arr[high]) = (arr[high], arr[i+1])
    return i + 1
def quick_sort(arr,low,high):
    if low < high:
        #find pivot elem such that elem smaller than pivot are on left
        # and greater than elem are on the right
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

def partition(arr, low, high):
    low, high = low, high
    if low != high and low < high:
        pivot = arr[low]
        low += 1
        while low <= high:
            if arr[high] < pivot and arr[low] > pivot:
                arr[high],arr[low] = arr[low],arr[high]
            if not arr[low] > pivot:
                low+=1
            if not arr[high] < pivot:
                high -= 1
        arr[low], arr[high] = arr[high], arr[low]
    return high

def quick_sort(array,low,high):
    if low < high:
        pi = partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
        

