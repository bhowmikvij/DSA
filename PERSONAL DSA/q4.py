# FUNCTION DEFINITION 
# TIME COMPLEXITY: O(log(m*n))

def search2DArray(arr, target):
    # number of rows
    m = len(arr)
    if m == 0:
        return False
    # number of columns
    n = len(arr[0])
    left, right = 0, m*n-1
    # binary search implementation
    while left <= right:
        mid = left+(right-left)//2
        # row_number -> mid//n
        # column_number -> mid%n
        mid_element = arr[mid//n][mid%n]
        if target == mid_element:
            return True
        elif target <= mid_element:
            right = mid-1
        else:
            left = mid+1
    return False


arr = [[1,2,3,4],[5,7,9,10],[12,14,15,18],[23,24,26,27]]
target = 34
result = search2DArray(arr,target)
print(result)