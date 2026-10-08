def merge_sorted_array(nums1, nums2):
    merged = []
    i, j = 0, 0 #two pointers
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1): #when nums2 runs out of elements, append the rest of nums1
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j]) #when nums1 runs out of elements, append the rest of nums2
        j += 1
    return merged

print(merge_sorted_array([1, 3, 5], [2, 4, 6])) # Output: [1, 2, 3, 4, 5, 6]