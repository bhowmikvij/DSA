# Find the maxima and minima using Divide and Conquer
# Using master's theorum: T(n) = O(n)
# Method Definition of MaxAndMin function


def findMaxAndMin(arr, i, j):
    # small problem - c
    # single element condition
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    # two element condition
    elif i == j-1:
        if arr[i] > arr[j]:
            max_val = arr[i]
            min_val = arr[j]
        else:
            max_val = arr[j]
            min_val = arr[i]
    else:
        # Divide and Conquer approach
        # 1. Divide
        mid = i + (j-i)//2
        # 2. Recursion
        max_1, min_1 = findMaxAndMin(arr, i, mid)
        max_2, min_2 = findMaxAndMin(arr, mid+1, j)
        # 3. Combine
        # To find the final maxima
        if min_1 < min_2:
            min_val = min_1
        else:
            min_val = min_2
        # To find the final minima
        if max_1 < max_2:
            max_val = max_2
        else:
            max_val = max_1

    return max_val, min_val    


# Driver Code
arr = [20, 39, 45, 65, 21, 44, 89, 92]
# i indicates the starting index
i = 0
# j indicates the ending index
j = len(arr) - 1
# function calling
max_val, min_val = findMaxAndMin(arr, i, j)
print('Maximum and Minimun value in the array is ', max_val, min_val)