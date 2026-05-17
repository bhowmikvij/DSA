# TWO POINTER APPROACH INTERVIEW QUESTION
def two_sum(arr, target_sum):
    left = 0
    right = len(arr)-1
    while left < right:
        if (arr[left] + arr[right] == target_sum):
            return left, right
        elif (arr[left] + arr[right] < target_sum):
            left += 1
        else:
            right -= 1
    return -1, -1

arr = [10, 20, 30, 40, 50, 60, 70, 90, 900]
target_sum = 150
result = two_sum(arr, target_sum)
print(result)