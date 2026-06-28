# Implementation of Bubble Sort
# Method Implementation
# Time COmplexity: O(n^2)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [70, 30, 20, 40, 58, 16, 78, 90]
result = bubbleSort(arr)
print("Array after using bubble sort is: ", result)