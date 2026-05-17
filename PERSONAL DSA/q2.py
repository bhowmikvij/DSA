# BINARY SEARCH (using recursion)
def binarySearch(arr, x, i, j):
    while i <= j:
        mid = i+(j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr, x, mid+1, j)
            # right side of the mid
            # search space - mid+1 to j
            # recursion - calling same function again inside the method definition
        else:
            # left side of the mid
            # search space - i to mid-1
            return binarySearch(arr, x, i, mid-1)
    # searching element is to present in an array
    return -1

arr = [20, 30, 40, 50, 60, 70]
x = 60
i = 0
j = len(arr)
# funtion calling
result = binarySearch(arr, x, i, j)
print(result)