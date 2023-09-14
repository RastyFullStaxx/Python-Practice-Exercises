def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

array1 = [1, 2, 2, 1]
array2 = [2, 2]
result = intersection(array1, array2)
print(result)
