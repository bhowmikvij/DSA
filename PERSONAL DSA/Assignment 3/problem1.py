# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to the target. [Amazon]
# You need to return the sum of three integers.

# For example: arr = [-1, 2, 1, -4], terget = 1
# Output: 2
# Explanation: [-1+2+1] = 2(The sum that is closest to the target is 2)


def threeSumClosest(nums, target):
    # At first we will sort the array
    nums.sort()
    # Then count number in array
    n = len(nums)

    closest_sum = nums[0] + nums[1] + nums[2]

    # Fix first number as i
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:

            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest_sum


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))