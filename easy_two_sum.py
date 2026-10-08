#Input:  nums = [2, 7, 11, 15], target = 9
#Output: [0, 1]

#Explanation: nums[0] + nums[1] = 2 + 7 = 9

'''def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] '''

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i] #indices of two numbers that add up to target
        num_dict[num] = i

print(twoSum([2, 7, 11, 15], 9))
