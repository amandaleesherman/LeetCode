'''def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1'''


def binary_search_recursive(nums, target, start, end): #start, mid, end are indices
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, end) #search right side
    else:
        return binary_search_recursive(nums, target, start, mid - 1) #search left side

print(binary_search_recursive([1, 2, 3, 4, 5], 3, 0, 4)) #2