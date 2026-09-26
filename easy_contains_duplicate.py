#Input:  nums = [1, 2, 3, 1]
#Output: True

#Explanation: The number 1 appears twice.

#hashtable soln
def containsDuplicate(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            return True
        num_dict[num] = 1
    return False

#set soln
'''def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False '''

print(containsDuplicate([1, 2, 3, 1]))
