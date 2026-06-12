def ternarySearch(arr, key, i, j):
    while i <= j:
        mid1 = i+(j-i)//3
        mid2 = j-(j-i)//3
        
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif arr[mid1] > key:
            return ternarySearch(arr, key, i, mid1-1)
        elif arr[mid2] < key:
            return ternarySearch(arr, key, mid2+1, j)
        else:
            return ternarySearch(arr, key, mid1+1, mid2-1)
    
    return -1


arr = [23, 56, 65, 78, 83, 85, 91, 93, 97, 99]
key = 98
i = 0
j = len(arr)-1
result = ternarySearch(arr, key, i, j)
print(result)