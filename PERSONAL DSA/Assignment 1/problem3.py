# Given a positive integer num, write a program that returns True if num is a perfect square else return False. Do not use built-in functions like sqrt. Also, talk about the time complexity of your code.
# Test Cases:
# Input: 16
# Output: True


def perfect_square(num):

    # your logic here
    left = 1
    right = num

    while left <= right:
        mid = left+(right-left)//2
        if mid*mid == num:
            return True
        elif mid*mid < num:
            left = mid+1
        else:
            right = mid-1
    return False



num = 101
result = perfect_square(num)
print(result)