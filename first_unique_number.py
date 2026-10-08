#Given an integer array nums, return the first number that appears exactly once. If no such number exists, return -1.
#Input:  [4, 1, 2, 1, 2, 4, 7]
#Output: 7

def firstUniqueNumber(nums): #dictionary
    num_dict = {}
    for num in nums:
        #if num in num_dict:
        #    num_dict[num] += 1
        #else:
        #    num_dict[num] = 1
        num_dict[num] = num_dict.get(num, 0) + 1
    for num in nums:
        if num_dict[num] == 1:
            return num
    return -1

#def firstUniqueNumber(nums): #hashmap
#    counts = {}
#    for num in nums:
#        counts[num] = counts.get(num, 0) + 1

#    for num in nums:
#        if counts[num] == 1:
#            return num

#    return -1