#Given an integer array nums, move all 0s to the end while maintaining the relative order of the non-zero elements.
#Example:
#Input:  [0,1,0,3,12]
#Output: [1,3,12,0,0]

def move_zeroes(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums

print(move_zeroes([0, 1, 0, 3, 12])) # Output: [1, 3, 12, 0, 0]