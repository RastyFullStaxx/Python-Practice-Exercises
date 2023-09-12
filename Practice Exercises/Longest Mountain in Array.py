def longest_mountain(arr):
    max_length = 0
    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left, right = i - 1, i + 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1
            while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                right += 1
            max_length = max(max_length, right - left + 1)
            i = right
        else:
            i += 1
    return max_length

mountain = [2, 1, 1, 5, 6, 2, 3, 1]
result = longest_mountain(mountain)
print(result)
