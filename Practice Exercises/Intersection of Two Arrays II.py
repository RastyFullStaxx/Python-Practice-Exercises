def intersect(nums1, nums2):
    from collections import Counter

    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    result = []

    for num, count in counter1.items():
        if num in counter2:
            result.extend([num] * min(count, counter2[num]))

    return result

# Example usage
array1 = [1, 2, 2, 1]
array2 = [2, 2]
result = intersect(array1, array2)
