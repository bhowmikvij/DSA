# SEARCHING --> Linear Search in an Array
# in list output should be 5


def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [23, 45, 56, 45, 60, 67, 78, 89, 93]
x = 67
result = linearsearch(arr, x)
print(result)

