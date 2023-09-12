def find_k_closest_elements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

array = [1, 2, 3, 4, 5]
k_value = 4
target_value = 3
result = find_k_closest_elements(array, k_value, target_value)
print(result)
