# Methos Definition
# Time Complexity: O(n^2)

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        # Swap happened after every pass
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


arr = [20, 34, 134, 14, 21, 54, 78, 98, 66, 81]
result = selectionSort(arr)
print(result)