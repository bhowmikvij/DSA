# Implementation of Insertion Sort
# Time complexity: O(n^2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]

        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [23, 34, 45, 56, 67, 78, 89]
result = insertion_sort(arr)
print(result)
